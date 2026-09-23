from cyphers.vigenere import cosets_vigenere
from breakers.break_caesar import break_caesar

def break_vigenere(ciphertext: str, m: int, language: str = "en") -> tuple[str, str]:
    """m is the key length, given to you. Returns (key, plaintext)."""

    cosets = cosets_vigenere(ciphertext, m)
    keys = []
    plaintext_unasembled= []

    for cos in cosets:
        key, plaintext = break_caesar(cos, language)
        keys.append(chr(key + ord('A')))
        plaintext_unasembled.append(plaintext)

    key = ''.join(keys)
    letters = [''] * sum(len(cos_plain) for cos_plain in plaintext_unasembled)
    for j, cos_plain in enumerate(plaintext_unasembled):
        for i, ch in enumerate(cos_plain):
            letters[i * m + j] = ch

    plaintext_chars = []
    letter_index = 0
    for ch in ciphertext.upper():
        if "A" <= ch <= "Z":
            plaintext_chars.append(letters[letter_index])
            letter_index += 1
        else:
            plaintext_chars.append(ch)

    plaintext = ''.join(plaintext_chars)
    return key, plaintext
