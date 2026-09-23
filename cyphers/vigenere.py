def vigenere(text: str, key: str, direction: int) -> str:
    # direction = 1 to encrypt, -1 to decrypt
    if len(key) == 0 or not key.isalpha():
        raise ValueError("Key must be a non-empty string of alphabetic characters.")
    key = key.upper()

    result = ""
    i = 0
    for c in text:
        if "A" <= c <= "Z":
            k = ord(key[i % len(key)]) - ord("A")
            c = chr((ord(c) - ord("A") + direction * k) % 26 + ord("A"))
            i += 1
        result += c
    return result


def encrypt_vigenere(plaintext: str, key: str) -> str:
    return vigenere(plaintext.upper().strip(), key, 1)


def decrypt_vigenere(ciphertext: str, key: str) -> str:
    return vigenere(ciphertext.upper(), key, -1)


def cosets_vigenere(ciphertext: str, m: int) -> list[str]:
    letters = [c for c in ciphertext.upper() if "A" <= c <= "Z"]
    return ["".join(letters[i::m]) for i in range(m)]
