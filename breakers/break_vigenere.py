from cyphers.vigenere import cosets_vigenere, decrypt_vigenere
from breakers.break_caesar import break_caesar


def break_vigenere(ciphertext: str, m: int, language: str = "en") -> tuple[str, str]:
    # m is the key length. Each coset is just a Caesar cipher, so break them one by one.
    key = ""
    for coset in cosets_vigenere(ciphertext, m):
        shift, _ = break_caesar(coset, language)
        key += chr(shift + ord("A"))
    return key, decrypt_vigenere(ciphertext, key).lower()
