from utils.basics import egcd, modinv, to_letters, to_numbers

def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    try:
        modinv(a, 26)
    except ValueError:
        raise ValueError(f"Invalid key: a={a} is not coprime with 26")
    return to_letters([(a * num + b) % 26 for num in to_numbers(plaintext.upper())])

def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    try:
        a_inv = modinv(a, 26)
    except ValueError:
        raise ValueError(f"Invalid key: a={a} is not coprime with 26")
    return to_letters([((num - b) * a_inv) % 26 for num in to_numbers(ciphertext)]).lower()

def valid_keys() -> list[tuple[int, int]]:
    valid_a = [a for a in range(1, 26) if egcd(a, 26)[0] == 1]
    return [(a, b) for a in valid_a for b in range(26)]
