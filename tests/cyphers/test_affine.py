import pytest

from cyphers.affine import affine_encrypt, affine_decrypt, valid_keys


class TestAffine:
    def test_affine_correctness(self):
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