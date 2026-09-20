from utils.basics import egcd, modinv

def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    try:
        modinv(a, 26)
    except ValueError:
        raise ValueError(f"Invalid key: a={a} is not coprime with 26")
    text = plaintext.upper().strip()
    return "".join(
        chr((a * (ord(c) - ord("A")) + b) % 26 + ord("A")) if "A" <= c <= "Z" else c
        for c in text
    )

def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    try:
        a_inv = modinv(a, 26)
    except ValueError:
        raise ValueError(f"Invalid key: a={a} is not coprime with 26")
    return "".join(
        chr(((ord(c) - ord("A") - b) * a_inv) % 26 + ord("A")) if "A" <= c <= "Z" else c
        for c in ciphertext
    ).lower()

def valid_keys() -> list[tuple[int, int]]:
    valid_a = [a for a in range(1, 26) if egcd(a, 26)[0] == 1]
    return [(a, b) for a in valid_a for b in range(26)]
