def encrypt(plaintext: str, key: int) -> str:
    text = plaintext.upper().strip()
    return "".join(
        chr((ord(c) - ord("A") + key) % 26 + ord("A")) if "A" <= c <= "Z" else c
        for c in text
    )

def decrypt(ciphertext: str, key: int) -> str:
    return "".join(
        chr((ord(c) - ord("A") - key) % 26 + ord("A")) if "A" <= c <= "Z" else c
        for c in ciphertext
    ).lower()
