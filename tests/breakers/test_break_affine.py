import pytest

from cyphers.affine import affine_encrypt, affine_decrypt
from breakers.break_affine import break_affine

class TestBreakAffine:
    def test_break_affine_english(self):
        plaintext = "Cryptography is the only branch of computing designed against an intelligent adaptive opponent A checksum protects you from a faulty cable It does not protect you from someone who wants"
        a, b = 5, 8
        ciphertext = affine_encrypt(plaintext, a, b)
        found_key, found_plaintext = break_affine(ciphertext, language="en")
        assert found_key == (a, b)
        assert found_plaintext == plaintext.lower()

    def test_break_affine_spanish(self):
        plaintext = "Ciencia que estudia la codificación de la información y permite su almacenamiento y transmisión en un formato inteligible solamente para las partes involucradas Es una herramienta útil para tratar los"
        a, b = 7, 3
        ciphertext = affine_encrypt(plaintext, a, b)
        found_key, found_plaintext = break_affine(ciphertext, language="es")
        assert found_key == (a, b)
        assert found_plaintext == plaintext.lower()