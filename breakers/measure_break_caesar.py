"""
Part C1 - measurement task for the Caesar breaker.

For each fragment length, take 200 random fragments of a reference text,
encrypt each with a random key, run break_caesar on it, and see how often
the recovered key matches the real one.

Run with:
    py -m breakers.measure_break_caesar
"""
import random

from cyphers.caesar import encrypt as caesar_encrypt
from breakers.break_caesar import break_caesar
from utils.constants import ENGLISH_TEXT, SPANISH_TEXT

LENGTHS = [20, 30, 40, 60, 100]
TRIALS = 200

random.seed(42)  # reproducible results


def random_fragment(text: str, length: int) -> str:
    """Pick a random substring of text that contains exactly "length" letters."""
    letter_positions = [i for i, c in enumerate(text) if c.isalpha()]
    start = random.randrange(len(letter_positions) - length + 1)
    first = letter_positions[start]
    last = letter_positions[start + length - 1]
    return text[first:last + 1]


def recovery_rate(text: str, length: int, table: str) -> float:
    correct = 0
    for _ in range(TRIALS):
        fragment = random_fragment(text, length)
        key = random.randrange(26)
        ciphertext = caesar_encrypt(fragment, key)
        found_key, _ = break_caesar(ciphertext, language=table)
        if found_key == key:
            correct += 1
    return correct / TRIALS


if __name__ == "__main__":
    print(f"{'len':>4} {'EN/EN':>8} {'EN/ES':>8} {'ES/ES':>8} {'ES/EN':>8}")
    for length in LENGTHS:
        en_en = recovery_rate(ENGLISH_TEXT, length, "en")
        en_es = recovery_rate(ENGLISH_TEXT, length, "es")
        es_es = recovery_rate(SPANISH_TEXT, length, "es")
        es_en = recovery_rate(SPANISH_TEXT, length, "en")
        print(f"{length:>4} {en_en:>8.1%} {en_es:>8.1%} {es_es:>8.1%} {es_en:>8.1%}")

# Answers
#
# 1) At which length does the breaker become reliable?
#    From 20 letters it's already above 90% with the right table, and by
#    30 letters it's basically always right (100% in my runs). Below that
#    there just isn't enough text for chi-squared to tell the real key
#    apart from the other 25 shifts.

# 2) How much does the wrong language table cost you?
#    It depends on which table is wrong. Using the English table on
#    Spanish text starts off costly for short texts (~35 points worse at
#    20 letters) but that gap almost disappears by 100 letters, so more
#    ciphertext fixes it. Using the Spanish table on English text is
#    worse and doesn't get better with length - it stays wrong a lot of
#    the time even at 100 letters. The Spanish table's letter shape
#    (extra letter, higher A/E weight) just doesn't match English well,
#    so guessing the wrong table isn't equally bad in both directions.
