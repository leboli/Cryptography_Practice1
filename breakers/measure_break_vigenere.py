"""
Part C3 - measurement task for the Vigenere breaker.

For each (key length, ciphertext length) pair, take 100 random fragments of
a reference text, encrypt each with a random key of that length, run
break_vigenere on it, and see how often the recovered key matches the real
one.

Run with:
    py -m breakers.measure_break_vigenere
"""
import random
import string

from cyphers.vigenere import encrypt_vigenere
from breakers.break_vigenere import break_vigenere
from utils.constants import ENGLISH_TEXT, SPANISH_TEXT

KEY_LENGTHS = [3, 5, 7]
LENGTHS = [60, 120, 200, 300]
TRIALS = 100

random.seed(42)  


def random_fragment(text: str, length: int) -> str:
    """Pick a random substring of text that contains exactly "length" letters."""
    letter_positions = [i for i, c in enumerate(text) if c.isalpha()]
    start = random.randrange(len(letter_positions) - length + 1)
    first = letter_positions[start]
    last = letter_positions[start + length - 1]
    return text[first:last + 1]


def random_key(m: int) -> str:
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(m))


def recovery_rate(text: str, length: int, m: int, table: str) -> float:
    correct = 0
    for _ in range(TRIALS):
        fragment = random_fragment(text, length)
        key = random_key(m)
        ciphertext = encrypt_vigenere(fragment, key)
        found_key, _ = break_vigenere(ciphertext, m, language=table)
        if found_key == key:
            correct += 1
    return correct / TRIALS


if __name__ == "__main__":
    for m in KEY_LENGTHS:
        print(f"key length m = {m}")
        print(f"{'len':>4} {'EN':>8} {'ES':>8} {'~coset len':>11}")
        for length in LENGTHS:
            en = recovery_rate(ENGLISH_TEXT, length, m, "en")
            es = recovery_rate(SPANISH_TEXT, length, m, "es")
            print(f"{length:>4} {en:>8.1%} {es:>8.1%} {length / m:>11.1f}")
        print()
