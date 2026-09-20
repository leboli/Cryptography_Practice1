from cyphers.caesar import decrypt as caesar_decrypt
from utils.constants import ENGLISH_FREQUENCY_TABLE, SPANISH_FREQUENCY_TABLE

def chi_squared(text: str, table: dict[str, float]) -> float:
    observed_counts = {letter: 0 for letter in table.keys()}
    total_letters = 0

    for char in text.upper():
        if char in observed_counts:
            observed_counts[char] += 1
            total_letters += 1

    if total_letters == 0:
        return float('inf')

    chi_squared_stat = 0.0
    for letter, expected_freq in table.items():
        expected_count = expected_freq * total_letters
        if expected_count > 0:
            chi_squared_stat += ((observed_counts[letter] - expected_count) ** 2) / expected_count

    return chi_squared_stat / total_letters

def break_caesar(ciphertext: str, language: str = "en") -> tuple[int, str]:
    frequency_table = ENGLISH_FREQUENCY_TABLE if language == "en" else SPANISH_FREQUENCY_TABLE

    best_key = 0
    lowest_chi_squared = float('inf')
    best_plaintext = ""

    for key in range(26):
        plaintext = caesar_decrypt(ciphertext, key)
        chi_squared_value = chi_squared(plaintext, frequency_table)

        if chi_squared_value < lowest_chi_squared:
            lowest_chi_squared = chi_squared_value
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext
