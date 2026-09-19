def encrypt_vigenere(plaintext: str, key: str) -> str:
    if len(key) == 0 or not key.isalpha():
        raise ValueError("Key must be a non-empty string of alphabetic characters.")

    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = ""

    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]

    for pi, ki in zip(plaintext, key):
        p_index = ord(pi) - ord('A')
        k_index = ord(ki) - ord('A')
        ciphertext += chr((p_index + k_index) % 26 + ord('A'))

    return ciphertext

def decrypt_vigenere(ciphertext: str, key: str) -> str:
    if len(key) == 0 or not key.isalpha():
        raise ValueError("Key must be a non-empty string of alphabetic characters.")

    key = key.upper()
    ciphertext = ciphertext.upper()
    plaintext = ""

    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]

    for ci, ki in zip(ciphertext, key):
        c_index = ord(ci) - ord('A')
        k_index = ord(ki) - ord('A')
        plaintext += chr((c_index - k_index + 26) % 26 + ord('A'))

    return plaintext

def cosets_vigenere(ciphertext: str, m: int) -> list[str]:
    return [ciphertext[i::m] for i in range(m)]
