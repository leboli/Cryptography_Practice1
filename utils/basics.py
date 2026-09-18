def to_numbers(text: str) -> list[int]: # normalised (uppercase) text -> 0..25
    return [ord(c) - ord("A") for c in text]


def to_letters(nums: list[int]) -> str: # 0..25 -> uppercase text
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return "".join([letters[i] for i in nums])


def egcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Euclidian algorithm. Returns (gcd, x, y) such that gcd = ax + by.
    """
    if b == 0:
        gcd, x, y = a, 1, 0
    else:
        gcd, x1, y1 = egcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        gcd = gcd
    if gcd < 0:
        gcd, x, y = -gcd, -x, -y
    return gcd, x, y


def modinv(a: int, m: int) -> int:
    egcd_result = egcd(a, m)
    if egcd_result[0] != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    else:
        return egcd_result[1] % m

def xor_bytes(data: bytes, key: bytes) -> bytes: # key repeats cyclically
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))
