from collections import Counter

from cyphers.caesar import decrypt as caesar_decrypt
from utils.constants import ENGLISH_FREQUENCY_TABLE, SPANISH_FREQUENCY_TABLE


def chi_squared(text: str, table: dict[str, float]) -> float:
    counts = Counter(c for c in text.upper() if c in table)
    total = sum(counts.values())
    if total == 0:
        return float("inf")

    chi = 0.0
    for letter, freq in table.items():
        expected = freq * total
        chi += (counts[letter] - expected) ** 2 / expected
    return chi / total


def break_caesar(ciphertext: str, language: str = "en") -> tuple[int, str]:
    table = ENGLISH_FREQUENCY_TABLE if language == "en" else SPANISH_FREQUENCY_TABLE
    # try all 26 shifts and keep the one that looks most like the language
    key = min(range(26), key=lambda k: chi_squared(caesar_decrypt(ciphertext, k), table))
    return key, caesar_decrypt(ciphertext, key)
