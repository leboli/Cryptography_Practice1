import pytest

from cyphers.vigenere import encrypt_vigenere
from breakers.break_vigenere import break_vigenere

class TestBreakVigenere:
    def test_break_vigenere_english_key_length_3(self):
        plaintext = ("Cryptography is the only branch of computing designed against an "
                     "intelligent adaptive opponent A checksum protects you from a faulty "
                     "cable It does not protect you from someone who wants your message to "
                     "arrive in a different form than you intended it")
        key = "KEY"
        ciphertext = encrypt_vigenere(plaintext, key)
        found_key, found_plaintext = break_vigenere(ciphertext, len(key), language="en")
        assert found_key == key
        assert found_plaintext == plaintext.lower()

    def test_break_vigenere_english_key_length_5(self):
        plaintext = ("Cryptography is the only branch of computing designed against an "
                     "intelligent adaptive opponent A checksum protects you from a faulty "
                     "cable It does not protect you from someone who wants your message to "
                     "arrive in a different form than you intended it")
        key = "CRYPT"
        ciphertext = encrypt_vigenere(plaintext, key)
        found_key, found_plaintext = break_vigenere(ciphertext, len(key), language="en")
        assert found_key == key
        assert found_plaintext == plaintext.lower()

    def test_break_vigenere_english_key_length_7(self):
        plaintext = ("Cryptography is the only branch of computing designed against an "
                     "intelligent adaptive opponent A checksum protects you from a faulty "
                     "cable It does not protect you from someone who wants your message to "
                     "arrive in a different form than you intended it")
        key = "NETWORK"
        ciphertext = encrypt_vigenere(plaintext, key)
        found_key, found_plaintext = break_vigenere(ciphertext, len(key), language="en")
        assert found_key == key
        assert found_plaintext == plaintext.lower()

    def test_break_vigenere_spanish_key_length_3(self):
        plaintext = ("Ciencia que estudia la codificacion de la informacion y permite su "
                     "almacenamiento y transmision en un formato inteligible solamente para "
                     "las partes involucradas Es una herramienta util para tratar los "
                     "problemas relacionados con la seguridad de los datos")
        key = "SOL"
        ciphertext = encrypt_vigenere(plaintext, key)
        found_key, found_plaintext = break_vigenere(ciphertext, len(key), language="es")
        assert found_key == key
        assert found_plaintext == plaintext.lower()

    def test_break_vigenere_spanish_key_length_5(self):
        plaintext = ("Ciencia que estudia la codificacion de la informacion y permite su "
                     "almacenamiento y transmision en un formato inteligible solamente para "
                     "las partes involucradas Es una herramienta util para tratar los "
                     "problemas relacionados con la seguridad de los datos")
        key = "PLAZA"
        ciphertext = encrypt_vigenere(plaintext, key)
        found_key, found_plaintext = break_vigenere(ciphertext, len(key), language="es")
        assert found_key == key
        assert found_plaintext == plaintext.lower()

    def test_break_vigenere_spanish_key_length_7(self):
        plaintext = ("Ciencia que estudia la codificacion de la informacion y permite su "
                     "almacenamiento y transmision en un formato inteligible solamente para "
                     "las partes involucradas Es una herramienta util para tratar los "
                     "problemas relacionados con la seguridad de los datos")
        key = "VENTANA"
        ciphertext = encrypt_vigenere(plaintext, key)
        found_key, found_plaintext = break_vigenere(ciphertext, len(key), language="es")
        assert found_key == key
        assert found_plaintext == plaintext.lower()

    def test_break_vigenere_preserves_punctuation_and_spacing(self):
        plaintext = ("Every single journey begins with just a simple step, no matter how "
                      "long or difficult the path may be. Cryptography is the only branch "
                      "of computing designed against an intelligent adaptive opponent!")
        key = "LEMON"
        ciphertext = encrypt_vigenere(plaintext, key)
        found_key, found_plaintext = break_vigenere(ciphertext, len(key), language="en")
        assert found_key == key
        assert found_plaintext == plaintext.lower()
