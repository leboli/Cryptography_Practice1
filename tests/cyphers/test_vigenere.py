import pytest

from cyphers.vigenere import encrypt_vigenere, decrypt_vigenere, cosets_vigenere

class TestVigenere:

    def test_correctness(self):
        plaintext = "hello"
        key = "KEY"
        ciphertext = encrypt_vigenere(plaintext, key)
        decrypted_text = decrypt_vigenere(ciphertext, key)
        assert decrypted_text == plaintext.upper()

    def test_invalid_key(self):
        plaintext = "hello"
        key = "123"  
        with pytest.raises(ValueError):
            encrypt_vigenere(plaintext, key)

    def test_invalid_key_empty(self):
        plaintext = "hello"
        key = ""  
        with pytest.raises(ValueError):
            encrypt_vigenere(plaintext, key)

    def test_cosets(self):
        ciphertext = "LXFOPVEFRNHR"
        m = 3
        expected_cosets = ['LOEN', 'XPFH', 'FVRR']
        assert cosets_vigenere(ciphertext, m) == expected_cosets

    def test01(self):
        plaintext = "mysecretmessage"
        key = "KEY"
        ciphertext = encrypt_vigenere(plaintext, key)
        assert ciphertext == "WCQOGPOXKOWQKKC"

    def test02(self):
        plaintext = "attackatdawn"
        key = "LEMON"
        ciphertext = encrypt_vigenere(plaintext, key)
        assert ciphertext == "LXFOPVEFRNHR"

    def test03(self):
        ciphertext = "ABCDEF"
        m = 3
        expected_cosets = ["AD", "BE", "CF"]
        assert cosets_vigenere(ciphertext, m) == expected_cosets
