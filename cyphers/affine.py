from utils.basics import egcd, modinv


def check_key(a: int):
    if egcd(a, 26)[0] != 1:
        raise ValueError(f"Invalid key: a={a} is not coprime with 26")


def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    check_key(a)
    result = ""
    for c in plaintext.upper().strip():
        if "A" <= c <= "Z":
            c = chr((a * (ord(c) - ord("A")) + b) % 26 + ord("A"))
        result += c
    return result


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    check_key(a)
    a_inv = modinv(a, 26)
    result = ""
    for c in ciphertext:
        if "A" <= c <= "Z":
            c = chr((ord(c) - ord("A") - b) * a_inv % 26 + ord("A"))
        result += c
    return result.lower()


def valid_keys() -> list[tuple[int, int]]:
    return [(a, b) for a in range(1, 26) if egcd(a, 26)[0] == 1 for b in range(26)]
