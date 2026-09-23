from breakers.break_caesar import chi_squared
from cyphers.affine import affine_decrypt, valid_keys
from utils.constants import ENGLISH_FREQUENCY_TABLE, SPANISH_FREQUENCY_TABLE


def break_affine(ciphertext: str, language: str = "en") -> tuple[tuple[int, int], str]:
    table = ENGLISH_FREQUENCY_TABLE if language == "en" else SPANISH_FREQUENCY_TABLE
    # only 12 * 26 = 312 keys, so just try them all
    a, b = min(valid_keys(), key=lambda k: chi_squared(affine_decrypt(ciphertext, *k), table))
    return (a, b), affine_decrypt(ciphertext, a, b)
