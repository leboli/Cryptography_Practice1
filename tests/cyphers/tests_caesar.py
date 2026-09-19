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

class TestMonoalphabetic:
    def test_key_from_keyword(self):
        from cyphers.monoalpha import key_from_keyword
        
        keyword = "CRYPTO"
        expected_key = "CRYPTOABDEFGHIJKLMNQSUVWXZ"
        generated_key = key_from_keyword(keyword)
        
        assert generated_key == expected_key

    def test_given1_encrypt_decrypt(self):
        from cyphers.monoalpha import encrypt_monoalphabetic, decrypt_monoalphabetic
        
        plaintext = "hello"
        key = "MNBVCXZASDFGHJKLPOIUYTREWQ"

        ciphertext = encrypt_monoalphabetic(plaintext, key)
        decrypted_text = decrypt_monoalphabetic(ciphertext, key)

        assert ciphertext == "ACGGK"
        assert decrypted_text == plaintext

    def test_given2_encrypt_decrypt(self):
        from cyphers.monoalpha import encrypt_monoalphabetic, decrypt_monoalphabetic

        plaintext = "bob"
        key = "MNBVCXZASDFGHJKLPOIUYTREWQ"
        
        ciphertext = encrypt_monoalphabetic(plaintext, key)
        decrypted_text = decrypt_monoalphabetic(ciphertext, key)

        assert ciphertext == "NKN"
        assert decrypted_text == plaintext

    def test_monoalphabetic_encrypt_decrypt(self):
        from cyphers.monoalpha import encrypt_monoalphabetic, decrypt_monoalphabetic, key_from_keyword
        
        plaintext = "hello"
        keyword = "keyword"
        key = key_from_keyword(keyword)
        
        ciphertext = encrypt_monoalphabetic(plaintext, key)
        decrypted_text = decrypt_monoalphabetic(ciphertext, key)
        
        assert decrypted_text == plaintext
    
    def test_monoalphabetic_invalid_key_length(self):
        from cyphers.monoalpha import encrypt_monoalphabetic
        
        plaintext = "hello"
        invalid_key = "SHORTKEY"  # Not 26 characters
        with pytest.raises(ValueError):
            encrypt_monoalphabetic(plaintext, invalid_key)

    def test_monoalphabetic_invalid_key_duplicates(self):
        from cyphers.monoalpha import encrypt_monoalphabetic

        plaintext = "hello"
        invalid_key = "AABBCCDDEEFFGGHHIIJJKKLLMM"  # Duplicates
        with pytest.raises(ValueError):
            encrypt_monoalphabetic(plaintext, invalid_key)