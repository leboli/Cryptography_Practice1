
# Tests

From the root run: 

```
py -m pytest tests/ -v
```

# C - Breakers

## C1 - Caesar breaker

Run the mesurements:

```
py -m breakers.measure_break_caesar
```

Recovery rate (200 fragmentos per length, fixed seed):

| len | EN/EN | EN/ES | ES/ES | ES/EN |
|-----|-------|-------|-------|-------|
| 20  | 95.0% | 65.0% | 99.0% | 57.0% |
| 30  | 100%  | 63.0% | 100%  | 77.5% |
| 40  | 100%  | 68.5% | 100%  | 83.0% |
| 60  | 100%  | 68.5% | 100%  | 93.5% |
| 100 | 100%  | 65.5% | 100%  | 100%  |

(EN/EN = english text with english table, EN/ES = english text with spanish table, ES/ES = spanish text with spanish table, ES/EN = spanish text with english table)

1) **At which length does the breaker become reliable?**

   From 20 letters it's already above 90% with the right table, and by 30 letters it's basically always right (100% in my runs). Below that there just isn't enough text for chi-squared to tell the real key apart from the other 25 shifts.

2) **How much does the wrong language table cost you?**

   It depends on which table is wrong. Using the English table on Spanish text starts off costly for short texts (35% worse at 20 letters) but that gap almost disappears by 100 letters, so more ciphertext fixes it. Using the Spanish table on English text is worse and doesn't get better with length, it stays wrong a lot of the time even at 100 letters. The Spanish table's letter shape (extra letter, higher A/E weight) just doesn't match English well, so guessing the wrong table isn't equally bad in both directions.

## C2 - Affine breaker

Run the mesurements:

```
py -m breakers.measure_break_affine
```

Recovery rate (200 fragmentos per length, fixed seed):

| len | EN/EN | EN/ES | ES/ES | ES/EN |
|-----|-------|-------|-------|-------|
| 20  | 83.5% | 34.5% | 89.0% | 42.5% |
| 30  | 96.0% | 38.5% | 96.5% | 40.0% |
| 40  | 98.0% | 38.0% | 99.5% | 65.0% |
| 60  | 100%  | 47.5% | 100%  | 66.0% |
| 100 | 100%  | 42.5% | 100%  | 86.0% |

(EN/EN = english text with english table, EN/ES = english text with spanish table, ES/ES = spanish text with spanish table, ES/EN = spanish text with english table)

1) **How many candidates did you test, and why is that the right number?**

   312 candidates per call: 12 valid values of `a` times 26 values of `b`. The valid `a` values are exactly the integers in 1..25 that are coprime with 26 (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25) . Any `a` sharing a factor with 26 isn't invertible mod 26, so it can't be a real affine key and decrypting with it would just be wrong. That's the whole key space, so testing all 312 is both necessary and sufficient. There's no valid key outside this set, and skipping any of them risks missing the real one.

2) **What's the shortest length at which recovery is reliable, and how does that compare to C1?**

   With the right table, affine only gets to 100% at 60 letters, versus 30 letters for the Caesar breaker in C1 (twice as much text needed). 
   
   The reason is the size of the key space: Caesar only has to pick the right answer out of 26 shifts, while affine has to pick it out of 312 (a, b) pairs. With a short, noisy fragment, chi-squared scores for the wrong keys are close together, and a bigger haystack of wrong keys means a higher chance that some wrong one scores lower than the true key just by luck. More ciphertext narrows the score gaps enough for the true key to win, so affine simply needs more letters to reach the same reliability.

## C3 - Vigenere breaker

Run the mesurements:

```
py -m breakers.measure_break_vigenere
```

Recovery rate (100 fragmentos per combination, fixed seed), each own-language text with its own table:

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

(`~coset len` = len / m, the average number of letters each individual Caesar sub-problem gets)

1) **What actually governs whether this works: total ciphertext length, or something else?**

   It's the coset length (len / m), not the total length. Look at len=60 with m=3 (coset len 20, 89-91% recovery) versus len=120 with m=7 (coset len 17.1, 72-77% recovery): the second one has *twice* the total ciphertext but does worse, because it's split across more cosets. Meanwhile len=200,m=7 (coset len 28.6, 95-100%) beats len=60,m=3 (coset len 20, 89-91%) despite having a longer key, simply because each coset still gets more letters. Rows with similar coset lengths land at similar recovery rates regardless of m or total length, which is the giveaway that coset length is the real variable, matching the same length-vs-reliability curve I saw for plain Caesar in C1.

2) **Why does a longer key make Vigenere stronger even though the cipher itself hasn't changed?**

   Breaking Vigenere with a known key length is just running the C1 Caesar attack m times, once per coset, and each coset only gets roughly 1/m of the ciphertext's letters. Chi-squared needs enough letters to tell the true shift's frequency profile apart from the other 25 by more than sampling noise; the same weakness reflected in C1. A longer key doesn't touch how any individual position is encrypted (it's still a Caesar shift), but it thins out how much evidence the attacker gets per key position, since the same ciphertext now has to cover more independent shifts. So the extra strength isn't in the encryption step, it's that a longer key starves each subproblem of the sample size cryptanalysis needs. Given enough ciphertext this advantage disappears (as the 300-length column shows, everything reaches 100% eventually), so "longer key = stronger" really means "stronger per unit of ciphertext available to the attacker."

# Use of LLM assistants

For this poject I used Claude Code for the following:

- Generating tests.
- Refinig the code for encryption and decryption in order to support text with spaces, punctuation and other characters. 
- Fixing a bug in the Vigenere coset reassembly and a mismatch between how the key index advances on encryption/decryption vs how cosets were split.
- Creating a measure base file for all the algorithms' breakers.
- Generating english and spanish text.
- Redacting answers and this file. 