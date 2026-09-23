ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def _validate_key(key: str) -> str:
    key = key.upper()
    if len(key) != 26 or len(set(key)) != 26 or not key.isalpha():
        raise ValueError("Key must be a permutation of the alphabet (26 unique letters)")
    return key

def encrypt_monoalphabetic(plaintext: str, key: str) -> str:
    """Encrypt plaintext using a monoalphabetic substitution cipher with the given key"""
    key = _validate_key(key)

    text = plaintext.upper().strip()
    return "".join(
        key[ord(c) - ord("A")] if "A" <= c <= "Z" else c
        for c in text
    )


def decrypt_monoalphabetic(ciphertext: str, key: str) -> str:
    """Decrypt ciphertext using a monoalphabetic substitution cipher with the given key"""
    key = _validate_key(key)

    return "".join(
        ALPHABET[key.index(c)] if "A" <= c <= "Z" else c
        for c in ciphertext.upper()
    ).lower()

def key_from_keyword(keyword: str) -> str:
    """Generate a monoalphabetic key from a keyword (keyword letters first, then remaining alphabet)"""
    keyword_upper = keyword.upper()

    if not all(c.isalpha() for c in keyword_upper):
        raise ValueError("Keyword must contain only letters")

    seen = set()
    key = []
    for char in keyword_upper:
        if char not in seen:
            seen.add(char)
            key.append(char)

    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in seen:
            key.append(char)

    return "".join(key)
