import pytest

from cyphers.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
from breakers.break_caesar import break_caesar, chi_squared, ENGLISH_FREQUENCY_TABLE, SPANISH_FREQUENCY_TABLE

class TestBreakCaesar:
    def test_break_caesar_english(self):
        plaintext = "Cryptography is the only branch of computing designed against an intelligent adaptive opponent A checksum protects you from a faulty cable It does not protect you from someone who wants"
        key = 6
        ciphertext = caesar_encrypt(plaintext, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="en")
        assert found_key == key
        assert found_plaintext == plaintext.lower()

    def test_break_caesar_spanish(self):
        plaintext = "Ciencia que estudia la codificación de la información y permite su almacenamiento y transmisión en un formato inteligible solamente para las partes involucradas Es una herramienta útil para tratar los"
        key = 5
        ciphertext = caesar_encrypt(plaintext, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="es")
        assert found_key == key
        assert found_plaintext == plaintext.lower()

    def test_chi_squared_statistic(self):
        text = "Cryptography is the only branch of computing designed against an intelligent adaptive opponent A checksum protects you from a faulty cable It does not protect you from someone who wants"
        chi_squared_value = chi_squared(text, ENGLISH_FREQUENCY_TABLE)
        assert isinstance(chi_squared_value, float)

    def test_chi_squared_statistic_spanish(self):
        text = "Ciencia que estudia la codificación de la información y permite su almacenamiento y transmisión en un formato inteligible solamente para las partes involucradas Es una herramienta útil para tratar los"
        chi_squared_value = chi_squared(text, SPANISH_FREQUENCY_TABLE)
        assert isinstance(chi_squared_value, float)

    def test_20_letters_english(self):
        text = "The sun shines so bright."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="en")
        assert found_key == key
        assert found_plaintext == text.lower()

    def test_20_letters_spanish(self):
        text = "La casa es muy bonita."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="es")
        assert found_key == key
        assert found_plaintext == text.lower()


    def test_30_letters_english(self):
        text = "Learning a new language is fun."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="en")
        assert found_key == key
        assert found_plaintext == text.lower()


    def test_30_letters_spanish(self):
        text = "Mañana viajaré con mi familia."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="es")
        assert found_key == key
        assert found_plaintext == text.lower()


    def test_40_letters_english(self):
        text = "Reading good books opens up a whole world."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="en")
        assert found_key == key
        assert found_plaintext == text.lower()


    def test_40_letters_spanish(self):
        text = "El perro corre rápido por el parque verde."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="es")
        assert found_key == key
        assert found_plaintext == text.lower()


    def test_60_letters_english(self):
        text = "Freshly brewed coffee in the morning always makes me happy."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="en")
        assert found_key == key
        assert found_plaintext == text.lower()


    def test_60_letters_spanish(self):
        text = "Me gusta caminar bajo la lluvia cuando las calles están vacías."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="es")
        assert found_key == key
        assert found_plaintext == text.lower()


    def test_100_letters_english(self):
        text = "Every single journey begins with just a simple step, no matter how long or difficult the path may be."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="en")
        assert found_key == key
        assert found_plaintext == text.lower()


    def test_100_letters_spanish(self):
        text = "Cuando miramos el cielo estrellado por la noche, nos damos cuenta de lo pequeño que es nuestro planeta."
        key = 3
        ciphertext = caesar_encrypt(text, key)
        found_key, found_plaintext = break_caesar(ciphertext, language="es")
        assert found_key == key
        assert found_plaintext == text.lower()