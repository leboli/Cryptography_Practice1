from utils.basics import to_letters, to_numbers

def _validate_key(key: str) -> None:
    if len(key) != 26 or len(set(key)) != 26:
        raise ValueError("Key must be a permutation of the alphabet (26 unique letters)")

def encrypt_monoalphabetic(plaintext: str, key: str) -> str:
    """Encrypt plaintext using a monoalphabetic substitution cipher with the given key"""
    _validate_key(key)

    positions_key = to_numbers(key)
    cipher_numbers = [positions_key[p] for p in to_numbers(plaintext.upper())]
    return to_letters(cipher_numbers)


def decrypt_monoalphabetic(ciphertext: str, key: str) -> str:
    """Decrypt ciphertext using a monoalphabetic substitution cipher with the given key"""
    _validate_key(key)

    positions_key = to_numbers(key)
    plain_numbers = [positions_key.index(c) for c in to_numbers(ciphertext)]
    return to_letters(plain_numbers).lower()

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
