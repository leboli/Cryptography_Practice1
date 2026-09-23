"""
Part C4 - report task for the frequency assistant.

Runs the assistant on the given 110-letter English cryptogram (22 distinct
letters) and checks the suggested initial mapping against the real key, so
we can answer the report-task questions in the README.

The real key was found by hand (helped by the report's own trigram/bigram
clues, then checked computationally against a large English corpus) - the
plaintext turns out to be a paraphrase of Kerckhoffs's principle. assist.py
itself never sees this key; it's only used here, after the fact, to grade
the suggested mapping.

Run with:
    py -m breakers.measure_assist
"""
from breakers.assist import clean_letters, suggested_mapping, report
from utils.constants import ENGLISH_FREQUENCY_TABLE

CRYPTOGRAM = """QATNT YSMHQ XJOCY HKATM FSNQI TUTMP TKTIP JIDTT KHIGQ ATCEG
JMHQA FNTYM TQRTY CSNTJ IEXQA TDTXY CIRTY ACIGT PVATI HQHNY
JFKMJ FHNTP"""

# Real key (cipher -> plain), recovered separately, not derived from assist.py.
TRUE_KEY = {
    'A': 'H', 'C': 'A', 'D': 'K', 'E': 'L', 'F': 'M', 'G': 'G', 'H': 'I',
    'I': 'N', 'J': 'O', 'K': 'P', 'M': 'R', 'N': 'S', 'O': 'F', 'P': 'D',
    'Q': 'T', 'R': 'B', 'S': 'U', 'T': 'E', 'U': 'V', 'V': 'W', 'X': 'Y',
    'Y': 'C',
}
TRUE_PLAINTEXT = (
    "THE SECURITY OF A CIPHER MUST NEVER DEPEND ON KEEPING THE ALGORITHM "
    "SECRET BECAUSE ONLY THE KEY CAN BE CHANGED WHEN IT IS COMPROMISED"
)


def mapping_accuracy(ciphertext: str, true_key: dict[str, str]) -> tuple[int, int]:
    """How many of the suggested mapping's guesses match the real key."""
    alphabet = set(ENGLISH_FREQUENCY_TABLE.keys())
    letters = clean_letters(ciphertext, alphabet)
    mapping = suggested_mapping(letters, ENGLISH_FREQUENCY_TABLE)
    correct = sum(1 for c, p in mapping.items() if true_key.get(c) == p)
    return correct, len(true_key)


if __name__ == "__main__":
    print(report(CRYPTOGRAM, "en"))
    print()

    correct, total = mapping_accuracy(CRYPTOGRAM, TRUE_KEY)
    print(f"Suggested mapping accuracy: {correct}/{total} letters correct")
    print(f"Real plaintext: {TRUE_PLAINTEXT}")

# Answers
#
# 1) How many of the 22 distinct letters does the suggested mapping get right?
#    3 out of 22 (T->E, U->V, X->Y). Run the script above to reproduce.
#
# 2) What's the single most useful line in the whole report for a human solver?
#    The repeated trigram line "QAT: count=3, positions=[1, 45, 74]". A
#    trigram that repeats 3 times in 110 letters, right at the start of the
#    text, is almost certainly "THE" - and unlike single-letter frequency,
#    that guess doesn't depend on this short sample matching the language's
#    overall letter distribution. It immediately pins down 3 letters at
#    once (Q, A, T) and, from there, the top bigrams AT ("HE") and QA ("TH")
#    confirm it.
#
# 3) Why does rank alignment alone not solve the cipher, and what does?
#    Rank alignment assumes this specific 110-letter sample's letter
#    frequencies land in the same order as the language's long-run average.
#    They don't: T is the cipher's most frequent letter at 18.2%, way above
#    English E's usual 12.6%, and letters like I and Q tie at 7.27% with no
#    way to break the tie correctly from frequency alone. Most letters in a
#    short sample are close enough in count that sampling noise reorders
#    them, so matching cipher-rank-i to language-rank-i is often just wrong,
#    which is exactly what the 3/22 score shows.
#    What actually solves it is the same thing a human solver does: use the
#    frequency ranking only as a rough starting point, then confirm or
#    correct each letter with structural evidence the ranking ignores -
#    repeated trigrams/bigrams matched to common words ("THE", "HE", "TH"),
#    doubled letters, and propagating each confirmed letter into the other
#    words it appears in until the partially-decoded text starts reading as
#    real English. That's what turned 3 correct guesses into the full
#    plaintext here.
