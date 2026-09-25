
# Tests

From the root run (`pytest.ini` puts the project root on the import path, so both work):

```
py -m pytest -v
pytest -v
```

Every cipher test file follows the same structure: the check values published in the handout, round-trip `decrypt(encrypt(m, k), k) == normalised m`, rejection of invalid keys, and edge cases (empty input, a single character, input with no letters, and for Vigenere input shorter than the key). Each breaker is tested on 20 generated ciphertexts per language at the length where the measurements below say it is reliable (Caesar 30 letters, affine 60, Vigenere ~40 letters per coset).

# Deviations from the handout

- **Folder layout.** The modules are grouped in folders instead of sitting at the root: `utils/basics.py`, `cyphers/{caesar,affine,monoalpha,vigenere}.py`, `breakers/{break_caesar,break_affine,break_vigenere,assist}.py`. Function names and signatures are exactly the ones in the handout.
- **Accents are folded, not dropped.** Input is normalised to uppercase A-Z as required, but accented letters are first reduced to their base letter (`É -> E`, `Ñ -> N`) instead of being removed, so Spanish text keeps all its letters. Because of this, the frequency of Ñ is added to N in the Spanish table.
- **Unknown languages are rejected.** Any `language` other than `"en"` or `"es"` raises `ValueError`.

# C - Breakers

## C1 - Caesar breaker

Run the measurements:

```
py -m breakers.measure_break_caesar
```

Recovery rate (200 fragments per length, fixed seed):

| len | EN/EN | EN/ES | ES/ES | ES/EN |
|-----|-------|-------|-------|-------|
| 20  | 95.0% | 65.0% | 99.0% | 57.0% |
| 30  | 100%  | 62.5% | 100%  | 77.5% |
| 40  | 100%  | 68.5% | 100%  | 83.0% |
| 60  | 100%  | 68.5% | 100%  | 93.5% |
| 100 | 100%  | 65.5% | 100%  | 100%  |

(EN/EN = english text with english table, EN/ES = english text with spanish table, ES/ES = spanish text with spanish table, ES/EN = spanish text with english table)

1) **At which length does the breaker become reliable?**

   From 20 letters it's already above 90% with the right table, and by 30 letters it's basically always right (100% in my runs). Below that there just isn't enough text for chi-squared to tell the real key apart from the other 25 shifts.

2) **How much does the wrong language table cost you?**

   It depends on which table is wrong. Using the English table on Spanish text starts off costly for short texts (35% worse at 20 letters) but that gap almost disappears by 100 letters, so more ciphertext fixes it. Using the Spanish table on English text is worse and doesn't get better with length, it stays wrong a lot of the time even at 100 letters. Looking at the failures at 100 letters, about two thirds of them pick the key off by exactly 13: under that wrong shift the common English letters N, R and H land on A, E and U, which are exactly the letters Spanish uses most, so the wrong decryption genuinely looks more Spanish than the right one. That is a systematic error, not noise, which is why more ciphertext doesn't fix it, and why guessing the wrong table isn't equally bad in both directions.

## C2 - Affine breaker

Run the measurements:

```
py -m breakers.measure_break_affine
```

Recovery rate (200 fragments per length, fixed seed):

| len | EN/EN | EN/ES | ES/ES | ES/EN |
|-----|-------|-------|-------|-------|
| 20  | 84.0% | 34.0% | 89.0% | 44.0% |
| 30  | 96.5% | 35.5% | 99.5% | 49.5% |
| 40  | 99.5% | 33.0% | 99.5% | 61.0% |
| 60  | 100%  | 40.0% | 100%  | 68.0% |
| 100 | 100%  | 41.0% | 100%  | 86.5% |

(EN/EN = english text with english table, EN/ES = english text with spanish table, ES/ES = spanish text with spanish table, ES/EN = spanish text with english table)

1) **How many candidates did you test, and why is that the right number?**

   312 candidates per call: 12 valid values of `a` times 26 values of `b`. The valid `a` values are exactly the integers in 1..25 that are coprime with 26 (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25) . Any `a` sharing a factor with 26 isn't invertible mod 26, so it can't be a real affine key and decrypting with it would just be wrong. That's the whole key space, so testing all 312 is both necessary and sufficient. There's no valid key outside this set, and skipping any of them risks missing the real one.

2) **What's the shortest length at which recovery is reliable, and how does that compare to C1?**

   With the right table, affine only gets to 100% at 60 letters, versus 30 letters for the Caesar breaker in C1 (twice as much text needed). 
   
   The reason is the size of the key space: Caesar only has to pick the right answer out of 26 shifts, while affine has to pick it out of 312 (a, b) pairs. With a short, noisy fragment, chi-squared scores for the wrong keys are close together, and a bigger haystack of wrong keys means a higher chance that some wrong one scores lower than the true key just by luck. More ciphertext narrows the score gaps enough for the true key to win, so affine simply needs more letters to reach the same reliability.

## C3 - Vigenere breaker

Run the measurements:

```
py -m breakers.measure_break_vigenere
```

Recovery rate (100 fragments per combination, fixed seed), each own-language text with its own table:

**m = 3**

| len | EN    | ES    | ~coset len |
|-----|-------|-------|------------|
| 60  | 89.0% | 91.0% | 20.0       |
| 120 | 100%  | 100%  | 40.0       |
| 200 | 100%  | 100%  | 66.7       |
| 300 | 100%  | 100%  | 100.0      |

**m = 5**

| len | EN    | ES    | ~coset len |
|-----|-------|-------|------------|
| 60  | 49.0% | 55.0% | 12.0       |
| 120 | 93.0% | 96.0% | 24.0       |
| 200 | 100%  | 100%  | 40.0       |
| 300 | 100%  | 100%  | 60.0       |

**m = 7**

| len | EN    | ES    | ~coset len |
|-----|-------|-------|------------|
| 60  | 13.0% | 17.0% | 8.6        |
| 120 | 72.0% | 77.0% | 17.1       |
| 200 | 95.0% | 100%  | 28.6       |
| 300 | 100%  | 100%  | 42.9       |

(`~coset len` = the average number of letters each individual Caesar sub-problem gets)

1) **What actually governs whether this works: total ciphertext length, or something else?**

   It's the coset length (len / m), not the total length. Look at len=60 with m=3 (coset len 20, 89-91% recovery) versus len=120 with m=7 (coset len 17.1, 72-77% recovery): the second one has *twice* the total ciphertext but does worse, because it's split across more cosets. Meanwhile len=200,m=7 (coset len 28.6, 95-100%) beats len=60,m=3 (coset len 20, 89-91%) despite having a longer key, simply because each coset still gets more letters. Rows with similar coset lengths land at similar recovery rates regardless of m or total length, which is the giveaway that coset length is the real variable, matching the same length-vs-reliability curve I saw for plain Caesar in C1.

2) **Why does a longer key make Vigenere stronger even though the cipher itself hasn't changed?**

   Breaking Vigenere with a known key length is just running the C1 Caesar attack m times, once per coset, and each coset only gets roughly 1/m of the ciphertext's letters. Chi-squared needs enough letters to tell the true shift's frequency profile apart from the other 25 by more than sampling noise; the same weakness reflected in C1. A longer key doesn't touch how any individual position is encrypted (it's still a Caesar shift), but it thins out how much evidence the attacker gets per key position, since the same ciphertext now has to cover more independent shifts. So the extra strength isn't in the encryption step, it's that a longer key starves each subproblem of the sample size cryptanalysis needs. Given enough ciphertext this advantage disappears (as the 300-length column shows, everything reaches 100% eventually), so "longer key = stronger" really means "stronger per unit of ciphertext available to the attacker."

## C4 - Frequency assistant for monoalphabetic substitution

Run it on the given cryptogram (and check the mapping against the real key):

```
py -m breakers.measure_assist
```

The cryptogram (110 letters, 22 distinct):

```
QATNT YSMHQ XJOCY HKATM FSNQI TUTMP TKTIP JIDTT KHIGQ ATCEG
JMHQA FNTYM TQRTY CSNTJ IEXQA TDTXY CIRTY ACIGT PVATI HQHNY
JFKMJ FHNTP
```

It decodes to a paraphrase of Kerckhoffs's principle: *"The security of a cipher must never depend on keeping the algorithm secret, because only the key can be changed when it is compromised."*

1) **How many of the 22 distinct letters does the suggested mapping get right?**

   3 out of 22 (T→E, U→V, X→Y).

2) **What's the single most useful line in the whole report for a human solver?**

   The repeated trigram line: `QAT: count=3, positions=[1, 45, 74]`. A trigram repeating 3 times in 110 letters, right at the start of the text, is almost certainly "THE", and that guess doesn't depend on this short sample's letters matching the language's long-run frequencies the way rank alignment does. It pins down 3 letters (Q, A, T) at once, and the top bigrams `AT` and `QA` immediately confirm it as "HE" and "TH".

3) **Why does rank alignment alone not solve the cipher, and what does?**

   Rank alignment assumes this one 110-letter sample's letter frequencies fall in the same order as the language's long-run average. They don't, T is the cipher's most frequent letter at 18.2%, well above English E's usual 12.6%, and several letters tie or sit close enough that sampling noise reorders them. Matching cipher-rank-i to language-rank-i is therefore often wrong, which is exactly why only 3 of 22 letters land correctly.

   What actually solves it is what a human solver does: treat the frequency ranking as a rough starting point only, then confirm or correct each letter with structural evidence the ranking ignores, repeated trigrams/bigrams matched to common words ("THE", "HE", "TH"), doubled letters, and propagating each confirmed letter into the other words it appears in until the partially-decoded text starts reading as real English.

# Use of LLM assistants

For this project I used Claude Code for the following:

- Generating tests.
- Refining the code for encryption and decryption in order to support text with spaces, punctuation and other characters. 
- Fixing a bug in the Vigenere coset reassembly and a mismatch between how the key index advances on encryption/decryption vs how cosets were split.
- Creating a measure base file for all the algorithms' breakers.
- Generating english and spanish text.
- Fixing a bug in the monoalphabetic cipher where decrypting lowercase/mixed-case ciphertext (or using a lowercase key) silently returned it unchanged instead of decrypting it.
- Building the C4 frequency assistant (`assist.py`) and its tests.
- Recovering the real key for the C4 cryptogram (used only in `measure_assist.py`, to grade the suggested mapping, never inside `assist.py` itself) with a quadgram-based hill-climbing/simulated-annealing search against public-domain English text, to know the ground truth for the report-task questions.
- Redacting answers and this file.
- Reviewing the whole project against the handout: renaming functions to the handout names, making every cipher go through `to_numbers`/`to_letters` (normalised output), stricter key validation (non A-Z letters in keys, empty XOR key, unknown language), and rewriting the tests so every part has check values, round-trips, invalid keys, edge cases and 20 generated ciphertexts per breaker. Measurements were re-run afterwards. 