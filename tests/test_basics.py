import pytest
from utils.basics import modinv, xor_bytes, egcd, to_numbers, to_letters


class TestModinv:
    """Test modular inverse function"""
    
    def test_modinv_basic_cases(self):
        assert modinv(5, 26) == 21
        assert modinv(7, 26) == 15
        assert modinv(17, 26) == 23
    
    def test_modinv_no_inverse(self):
        with pytest.raises(ValueError):
            modinv(13, 26)
        with pytest.raises(ValueError):
            modinv(2, 26)
    
    def test_modinv_negative_input(self):
        # (-3 * x) ≡ 1 (mod 7) => x = 5 (since -3 ≡ 4 mod 7)
        result = modinv(-3, 7)
        assert ((-3 * result) % 7) == 1
    
    def test_modinv_prime_modulus(self):
        # For prime p, modinv exists for all a in 1..p-1
        assert modinv(1, 11) == 1
        assert modinv(2, 11) == 6
        assert modinv(5, 11) == 9
    
    def test_modinv_with_1(self):
        assert modinv(1, 100) == 1
    
    def test_modinv_large_numbers(self):
        # modinv(123, 1000007) should work (1000007 is prime)
        result = modinv(123, 1000007)
        assert (123 * result) % 1000007 == 1
    
    def test_modinv_error_message_includes_value(self):
        with pytest.raises(ValueError) as exc_info:
            modinv(4, 8)
        assert "4" in str(exc_info.value)


class TestXorBytes:
    """Test XOR encryption with repeating key"""
    
    def test_xor_basic(self):
        assert xor_bytes(b"HELLO", b"KEYKE").hex() == "030015070a"
    
    def test_xor_roundtrip_property(self):
        # xor_bytes(xor_bytes(d, k), k) == d
        data = b"HELLO WORLD"
        key = b"SECRET"
        encrypted = xor_bytes(data, key)
        decrypted = xor_bytes(encrypted, key)
        assert decrypted == data
    
    def test_xor_empty_data(self):
        result = xor_bytes(b"", b"KEY")
        assert result == b""
    
    def test_xor_single_byte_key(self):
        data = b"HELLO"
        key = b"X"
        encrypted = xor_bytes(data, key)
        decrypted = xor_bytes(encrypted, key)
        assert decrypted == data
    
    def test_xor_key_longer_than_data(self):
        data = b"HI"
        key = b"VERYLONGKEY"
        encrypted = xor_bytes(data, key)
        decrypted = xor_bytes(encrypted, key)
        assert decrypted == data
    
    def test_xor_binary_data(self):
        data = bytes([0, 1, 127, 128, 255])
        key = bytes([42])
        encrypted = xor_bytes(data, key)
        decrypted = xor_bytes(encrypted, key)
        assert decrypted == data
    
    def test_xor_zero_bytes_in_data(self):
        data = b"\x00\x00\x00"
        key = b"ABC"
        encrypted = xor_bytes(data, key)
        # Encrypted should be equal to key (0 XOR x = x)
        assert encrypted == key
    
    def test_xor_same_data_and_key(self):
        data = b"TEST"
        key = b"TEST"
        encrypted = xor_bytes(data, key)
        # Any byte XOR itself is 0
        assert encrypted == b"\x00\x00\x00\x00"


class TestEgcd:
    """Test extended GCD function"""
    
    def test_egcd_basic(self):
        gcd, x, y = egcd(30, 12)
        assert gcd == 6
        assert 30 * x + 12 * y == 6
    
    def test_egcd_coprime(self):
        gcd, x, y = egcd(7, 5)
        assert gcd == 1
        assert 7 * x + 5 * y == 1
    
    def test_egcd_negative_inputs(self):
        gcd, x, y = egcd(-30, 12)
        assert gcd == 6
        assert -30 * x + 12 * y == 6
    
    def test_egcd_both_negative(self):
        gcd, x, y = egcd(-30, -12)
        assert gcd == 6
        assert -30 * x + (-12) * y == 6
    
    def test_egcd_with_zero(self):
        gcd, x, y = egcd(5, 0)
        assert gcd == 5
        assert 5 * x + 0 * y == 5
    
    def test_egcd_bezout_identity(self):
        # General test: gcd = a*x + b*y must hold
        for a, b in [(17, 13), (100, 35), (-42, 28)]:
            gcd, x, y = egcd(a, b)
            assert a * x + b * y == gcd


class TestToNumbers:
    """Test text to number conversion"""
    
    def test_to_numbers_basic(self):
        assert to_numbers("abc") == [0, 1, 2]
    
    def test_to_numbers_full_alphabet(self):
        result = to_numbers("abcdefghijklmnopqrstuvwxyz")
        assert result == list(range(26))
    
    def test_to_numbers_single_letter(self):
        assert to_numbers("z") == [25]
    
    def test_to_numbers_repeated(self):
        assert to_numbers("aaa") == [0, 0, 0]


class TestToLetters:
    """Test number to text conversion"""
    
    def test_to_letters_basic(self):
        assert to_letters([0, 1, 2]) == "abc"
    
    def test_to_letters_full_range(self):
        assert to_letters(list(range(26))) == "abcdefghijklmnopqrstuvwxyz"
    
    def test_to_letters_single(self):
        assert to_letters([25]) == "z"
    
    def test_to_letters_empty(self):
        assert to_letters([]) == ""


class TestRoundtrips:
    """Test conversions roundtrip correctly"""
    
    def test_numbers_to_letters_roundtrip(self):
        original = "thequickbrownfox"
        nums = to_numbers(original)
        result = to_letters(nums)
        assert result == original
    
    def test_letters_to_numbers_roundtrip(self):
        original = [5, 10, 15, 20, 25, 0]
        letters = to_letters(original)
        result = to_numbers(letters)
        assert result == original