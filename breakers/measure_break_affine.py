"""
Part C2 - measurement task for the Affine breaker.

For each fragment length, take 200 random fragments of a reference text,
encrypt each with a random key, run break_affine on it, and see how often
the recovered key matches the real one.

Run with:
    py -m breakers.measure_break_affine
"""
import random

from cyphers.affine import affine_encrypt
from breakers.break_affine import break_affine
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
    possible_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    correct = 0
    for _ in range(TRIALS):
        fragment = random_fragment(text, length)
        a = random.choice(possible_a)
        b = random.randrange(26)
        ciphertext = affine_encrypt(fragment, a, b)
        found_key, _ = break_affine(ciphertext, language=table)
        if found_key == (a, b):
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
