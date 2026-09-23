ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def check_key(key: str) -> str:
    key = key.upper()
    if len(key) != 26 or len(set(key)) != 26 or not key.isalpha():
        raise ValueError("Key must be a permutation of the alphabet (26 unique letters)")
    return key


def encrypt_monoalphabetic(plaintext: str, key: str) -> str:
    key = check_key(key)
    result = ""
    for c in plaintext.upper().strip():
        if "A" <= c <= "Z":
            c = key[ord(c) - ord("A")]
        result += c
    return result


def decrypt_monoalphabetic(ciphertext: str, key: str) -> str:
    key = check_key(key)
    result = ""
    for c in ciphertext.upper():
        if "A" <= c <= "Z":
            c = ALPHABET[key.index(c)]
        result += c
    return result.lower()


def key_from_keyword(keyword: str) -> str:
    # keyword letters first (no repeats), then the rest of the alphabet
    keyword = keyword.upper()
    if not all(c.isalpha() for c in keyword):
        raise ValueError("Keyword must contain only letters")

    key = ""
    for c in keyword + ALPHABET:
        if c not in key:
            key += c
    return key
