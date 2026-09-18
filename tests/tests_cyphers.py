import pytest

from cyphers.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
from cyphers.affine import affine_encrypt, affine_decrypt, valid_keys

class TestCaesar:
    def test_caesar_encrypt_decrypt(self):
        plaintext = "hello"
        key = 3
        ciphertext = caesar_encrypt(plaintext, key)
        decrypted_text = caesar_decrypt(ciphertext, key)
        assert decrypted_text == plaintext
    
    def test_caesar_encrypt_with_wraparound(self):
        plaintext = "xyz"
        key = 3
        ciphertext = caesar_encrypt(plaintext, key)
        assert ciphertext == "abc"
    
    def test_caesar_decrypt_with_wraparound(self):
        ciphertext = "abc"
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

class TestAffine:
    def test_affine_encrypt_decrypt(self):
        plaintext = "hello"
        a, b = 5, 8
        ciphertext = affine_encrypt(plaintext, a, b)
        decrypted_text = affine_decrypt(ciphertext, a, b)
        assert decrypted_text == plaintext
    
    def test_affine_invalid_key(self):
        plaintext = "hello"
        a, b = 13, 5  # 13 is not coprime with 26
        with pytest.raises(ValueError):
            affine_encrypt(plaintext, a, b)
            