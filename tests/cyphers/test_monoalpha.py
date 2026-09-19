import pytest

from cyphers.monoalpha import key_from_keyword
from cyphers.monoalpha import encrypt_monoalphabetic, decrypt_monoalphabetic

class TestMonoalphabetic:
    def test_key_from_keyword(self):
        
        keyword = "CRYPTO"
        expected_key = "CRYPTOABDEFGHIJKLMNQSUVWXZ"
        generated_key = key_from_keyword(keyword)
        
        assert generated_key == expected_key

    def test_given1_encrypt_decrypt(self):
        
        plaintext = "hello"
        key = "MNBVCXZASDFGHJKLPOIUYTREWQ"

        ciphertext = encrypt_monoalphabetic(plaintext, key)
        decrypted_text = decrypt_monoalphabetic(ciphertext, key)

        assert ciphertext == "ACGGK"
        assert decrypted_text == plaintext

    def test_given2_encrypt_decrypt(self):

        plaintext = "bob"
        key = "MNBVCXZASDFGHJKLPOIUYTREWQ"
        
        ciphertext = encrypt_monoalphabetic(plaintext, key)
        decrypted_text = decrypt_monoalphabetic(ciphertext, key)

        assert ciphertext == "NKN"
        assert decrypted_text == plaintext

    def test_monoalphabetic_correctness(self):
        
        plaintext = "hello"
        keyword = "keyword"
        key = key_from_keyword(keyword)
        
        ciphertext = encrypt_monoalphabetic(plaintext, key)
        decrypted_text = decrypt_monoalphabetic(ciphertext, key)
        
        assert decrypted_text == plaintext
    
    def test_monoalphabetic_invalid_key_length(self):
        
        plaintext = "hello"
        invalid_key = "SHORTKEY"  # Not 26 characters
        with pytest.raises(ValueError):
            encrypt_monoalphabetic(plaintext, invalid_key)

    def test_monoalphabetic_invalid_key_duplicates(self):

        plaintext = "hello"
        invalid_key = "AABBCCDDEEFFGGHHIIJJKKLLMM"  # Duplicates
        with pytest.raises(ValueError):
            encrypt_monoalphabetic(plaintext, invalid_key)