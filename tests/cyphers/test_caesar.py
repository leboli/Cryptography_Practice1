import pytest

from cyphers.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt

class TestCaesar:
    def test_caesar_correctness(self):
        plaintext = "hello"
        key = 3
        ciphertext = caesar_encrypt(plaintext, key)
        decrypted_text = caesar_decrypt(ciphertext, key)
        assert decrypted_text == plaintext
    
    def test_caesar_encrypt_with_wraparound(self):
        plaintext = "xyz"
        key = 3
        ciphertext = caesar_encrypt(plaintext, key)
        assert ciphertext == "ABC"

    def test_caesar_decrypt_with_wraparound(self):
        ciphertext = "ABC"
        key = 3
        decrypted_text = caesar_decrypt(ciphertext, key)
        assert decrypted_text == "xyz"
    
    def test_caesar_encrypt_empty_string(self):
        plaintext = ""
        key = 5
        ciphertext = caesar_encrypt(plaintext, key)
        assert ciphertext == ""
    
    def test_caesar_decrypt_empty_string(self):
        ciphertext = ""
        key = 5
        decrypted_text = caesar_decrypt(ciphertext, key)
        assert decrypted_text == ""
