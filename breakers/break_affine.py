from breakers.break_caesar import chi_squared
from cyphers.affine import affine_decrypt
from utils.constants import ENGLISH_FREQUENCY_TABLE, SPANISH_FREQUENCY_TABLE

def break_affine(ciphertext: str, language: str = "en") -> tuple[tuple[int, int], str]:
    best_key = (0, 0)
    lowest_chi_squared = float('inf')
    best_plaintext = ""

    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            plaintext = affine_decrypt(ciphertext, a, b)
            chi_squared_value = chi_squared(plaintext, ENGLISH_FREQUENCY_TABLE if language == "en" else SPANISH_FREQUENCY_TABLE)

            if chi_squared_value < lowest_chi_squared:
                lowest_chi_squared = chi_squared_value
                best_key = (a, b)
                best_plaintext = plaintext

    return best_key, best_plaintext