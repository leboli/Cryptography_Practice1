def encrypt_vigenere(plaintext: str, key: str) -> str:
    if len(key) == 0 or not key.isalpha():
        raise ValueError("Key must be a non-empty string of alphabetic characters.")

    key = key.upper()
    plaintext = plaintext.upper().strip()
    ciphertext = ""
    key_index = 0

    for pi in plaintext:
        if "A" <= pi <= "Z":
            p_index = ord(pi) - ord('A')
            k_index = ord(key[key_index % len(key)]) - ord('A')
            ciphertext += chr((p_index + k_index) % 26 + ord('A'))
            key_index += 1
        else:
            ciphertext += pi

    return ciphertext

def decrypt_vigenere(ciphertext: str, key: str) -> str:
    if len(key) == 0 or not key.isalpha():
        raise ValueError("Key must be a non-empty string of alphabetic characters.")

    key = key.upper()
    ciphertext = ciphertext.upper()
    plaintext = ""
    key_index = 0

    for ci in ciphertext:
        if "A" <= ci <= "Z":
            c_index = ord(ci) - ord('A')
            k_index = ord(key[key_index % len(key)]) - ord('A')
            plaintext += chr((c_index - k_index + 26) % 26 + ord('A'))
            key_index += 1
        else:
            plaintext += ci

    return plaintext

def cosets_vigenere(ciphertext: str, m: int) -> list[str]:
    return [ciphertext[i::m] for i in range(m)]
