def shift(text: str, key: int) -> str:
    result = ""
    for c in text:
        if "A" <= c <= "Z":
            c = chr((ord(c) - ord("A") + key) % 26 + ord("A"))
        result += c
    return result


def encrypt(plaintext: str, key: int) -> str:
    return shift(plaintext.upper().strip(), key)


def decrypt(ciphertext: str, key: int) -> str:
    return shift(ciphertext, -key).lower()
