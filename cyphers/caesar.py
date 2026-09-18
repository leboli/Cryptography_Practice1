from utils.basics import to_numbers, to_letters

def encrypt(plaintext: str, key: int) -> str:
    plain_numbers = to_numbers(plaintext)
    cipher_numbers = [(num + key) % 26 for num in plain_numbers]
    return to_letters(cipher_numbers)

def decrypt(ciphertext: str, key: int) -> str:
    cipher_numbers = to_numbers(ciphertext)
    plain_numbers = [(num - key) % 26 for num in cipher_numbers]
    return to_letters(plain_numbers)


