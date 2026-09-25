import pytest

from utils.basics import normalise, to_numbers, to_letters, egcd, modinv, xor_bytes


class TestCheckValues:
    """Values published in the handout (Part A)"""

    def test_modinv_values(self):
        assert modinv(5, 26) == 21
        assert modinv(7, 26) == 15
        assert modinv(17, 26) == 23

    def test_modinv_raises(self):
        with pytest.raises(ValueError):
            modinv(13, 26)
        with pytest.raises(ValueError):
            modinv(2, 26)

    def test_xor_value(self):
        assert xor_bytes(b"HELLO", b"KEYKE").hex() == "030015070a"


class TestNormalise:
    def test_uppercases_and_removes_non_letters(self):
        assert normalise("Hello, World! 123") == "HELLOWORLD"

    def test_folds_accents(self):
        assert normalise("Mañana, canción") == "MANANACANCION"

    def test_no_letters(self):
        assert normalise("123 !?") == ""


class TestToNumbersToLetters:
    def test_to_numbers(self):
        assert to_numbers("ABC") == [0, 1, 2]
        assert to_numbers("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == list(range(26))

    def test_to_numbers_normalises_input(self):
        assert to_numbers("a b, c!") == [0, 1, 2]

    def test_to_letters(self):
        assert to_letters([0, 1, 2]) == "ABC"
        assert to_letters(list(range(26))) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def test_round_trip(self):
        assert to_letters(to_numbers("THEQUICKBROWNFOX")) == "THEQUICKBROWNFOX"
        assert to_numbers(to_letters([5, 10, 15, 20, 25, 0])) == [5, 10, 15, 20, 25, 0]

    def test_to_letters_rejects_out_of_range(self):
        with pytest.raises(ValueError):
            to_letters([26])
        with pytest.raises(ValueError):
            to_letters([-1])

    def test_edge_cases(self):
        assert to_numbers("") == []
        assert to_numbers("!!!") == []
        assert to_numbers("z") == [25]
        assert to_letters([]) == ""


class TestEgcd:
    @pytest.mark.parametrize("a, b, expected_gcd", [
        (30, 12, 6), (7, 5, 1), (17, 13, 1), (100, 35, 5), (5, 0, 5), (0, 5, 5),
    ])
    def test_bezout_identity(self, a, b, expected_gcd):
        gcd, x, y = egcd(a, b)
        assert gcd == expected_gcd
        assert a * x + b * y == gcd

    @pytest.mark.parametrize("a, b", [(-30, 12), (30, -12), (-30, -12), (-42, 28), (-7, 26)])
    def test_negative_inputs(self, a, b):
        gcd, x, y = egcd(a, b)
        assert gcd > 0
        assert a * x + b * y == gcd


class TestModinv:
    def test_inverse_for_every_valid_a_mod_26(self):
        for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
            inv = modinv(a, 26)
            assert 0 <= inv < 26
            assert (a * inv) % 26 == 1

    def test_negative_input(self):
        assert modinv(-3, 7) == 2          # -3 * 2 = -6 = 1 (mod 7)
        assert modinv(-5, 26) == 5         # -5 is 21 mod 26, and 21 * 5 = 105 = 1 (mod 26)

    def test_large_numbers(self):
        assert (123 * modinv(123, 1000007)) % 1000007 == 1

    def test_error_message_names_the_value(self):
        with pytest.raises(ValueError, match="13"):
            modinv(13, 26)

    def test_rejects_every_a_not_coprime_with_26(self):
        for a in [0, 2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24, 26]:
            with pytest.raises(ValueError):
                modinv(a, 26)

    def test_does_not_search(self):
        # a search loop over range(m) would take forever here, egcd is instant
        m = 10 ** 30 + 57
        assert (7 * modinv(7, m)) % m == 1


class TestXorBytes:
    @pytest.mark.parametrize("data, key", [
        (b"HELLO WORLD", b"SECRET"),
        (b"HELLO", b"X"),                          # single byte key
        (b"HI", b"VERYLONGKEY"),                   # key longer than data
        (bytes([0, 1, 127, 128, 255]), bytes([42])),
        (b"", b"KEY"),                             # empty data
    ])
    def test_round_trip(self, data, key):
        assert xor_bytes(xor_bytes(data, key), key) == data

    def test_key_repeats_cyclically(self):
        assert xor_bytes(b"\x00\x00\x00\x00\x00", b"AB") == b"ABABA"

    def test_same_data_and_key_gives_zeros(self):
        assert xor_bytes(b"TEST", b"TEST") == b"\x00\x00\x00\x00"

    def test_empty_key_rejected(self):
        with pytest.raises(ValueError):
            xor_bytes(b"HELLO", b"")
