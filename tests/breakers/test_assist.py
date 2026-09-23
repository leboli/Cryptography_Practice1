import pytest

from breakers.assist import (
    clean_letters,
    ngrams,
    letter_frequencies,
    repeated_ngrams,
    top_bigrams,
    doubled_letters,
    suggested_mapping,
    report,
)
from utils.constants import ENGLISH_FREQUENCY_TABLE, SPANISH_FREQUENCY_TABLE

CRYPTOGRAM = (
    "QATNT YSMHQ XJOCY HKATM FSNQI TUTMP TKTIP JIDTT KHIGQ ATCEG "
    "JMHQA FNTYM TQRTY CSNTJ IEXQA TDTXY CIRTY ACIGT PVATI HQHNY "
    "JFKMJ FHNTP"
)


class TestCleanLetters:
    def test_strips_spaces_punctuation_and_digits(self):
        alphabet = set(ENGLISH_FREQUENCY_TABLE.keys())
        assert clean_letters("Hi, there! 123", alphabet) == "HITHERE"

    def test_uppercases_input(self):
        alphabet = set(ENGLISH_FREQUENCY_TABLE.keys())
        assert clean_letters("abc", alphabet) == "ABC"

    def test_drops_letters_outside_the_language_alphabet(self):
        # Ñ is not part of ENGLISH_FREQUENCY_TABLE
        alphabet = set(ENGLISH_FREQUENCY_TABLE.keys())
        assert clean_letters("NIÑO", alphabet) == "NIO"

    def test_keeps_n_tilde_for_spanish(self):
        alphabet = set(SPANISH_FREQUENCY_TABLE.keys())
        assert clean_letters("NIÑO", alphabet) == "NIÑO"


class TestNgrams:
    def test_bigrams(self):
        assert ngrams("ABCD", 2) == ["AB", "BC", "CD"]

    def test_trigrams(self):
        assert ngrams("ABCD", 3) == ["ABC", "BCD"]

    def test_shorter_than_n_returns_empty(self):
        assert ngrams("AB", 3) == []


class TestLetterFrequencies:
    def test_counts_and_percentages(self):
        freqs = letter_frequencies("AAAB")
        assert freqs == [("A", 3, 75.0), ("B", 1, 25.0)]

    def test_ties_broken_alphabetically(self):
        freqs = letter_frequencies("BA")
        assert freqs == [("A", 1, 50.0), ("B", 1, 50.0)]


class TestRepeatedNgrams:
    def test_finds_repeated_trigram_with_positions(self):
        # "ABC" at position 1 and position 5 (1-indexed)
        repeated = repeated_ngrams("ABCXXABC", 3)
        assert repeated == {"ABC": [1, 6]}

    def test_no_repeats_returns_empty(self):
        assert repeated_ngrams("ABCDEF", 3) == {}


class TestTopBigrams:
    def test_ranks_by_count_then_alphabetically(self):
        top = top_bigrams("ABABCD", n=2)
        assert top[0] == ("AB", 2, pytest.approx(40.0))

    def test_respects_n_limit(self):
        top = top_bigrams("ABCDEFGHIJ", n=3)
        assert len(top) == 3


class TestDoubledLetters:
    def test_finds_doubled_letters_with_positions(self):
        assert doubled_letters("HELLO") == {"L": [3]}

    def test_multiple_doubles(self):
        assert doubled_letters("AABBCC") == {"A": [1], "B": [3], "C": [5]}

    def test_no_doubles(self):
        assert doubled_letters("ABC") == {}


class TestSuggestedMapping:
    def test_aligns_most_frequent_cipher_letter_to_most_frequent_plaintext_letter(self):
        mapping = suggested_mapping("TTTTAAABB", ENGLISH_FREQUENCY_TABLE)
        assert mapping["T"] == "E"  # most frequent English letter

    def test_covers_every_distinct_cipher_letter(self):
        letters = "TTTAAABBC"
        mapping = suggested_mapping(letters, ENGLISH_FREQUENCY_TABLE)
        assert set(mapping.keys()) == set(letters)


class TestReport:
    def test_contains_required_sections(self):
        text = report(CRYPTOGRAM, "en")
        assert "LETTER FREQUENCIES" in text
        assert "REPEATED TRIGRAMS" in text
        assert "TOP 10 MOST FREQUENT BIGRAMS" in text
        assert "DOUBLED LETTERS" in text
        assert "SUGGESTED INITIAL MAPPING" in text

    def test_reports_correct_letter_counts_for_the_given_cryptogram(self):
        text = report(CRYPTOGRAM, "en")
        assert "Total letters analyzed: 110" in text
        assert "Distinct ciphertext letters: 22" in text

    def test_finds_the_known_repeated_trigram(self):
        text = report(CRYPTOGRAM, "en")
        assert "QAT: count=3" in text

    def test_finds_the_known_doubled_letter(self):
        text = report(CRYPTOGRAM, "en")
        assert "TT: count=1" in text

    def test_defaults_to_english(self):
        assert report(CRYPTOGRAM) == report(CRYPTOGRAM, "en")

    def test_spanish_report_uses_spanish_tables(self):
        text = report(CRYPTOGRAM, "es")
        assert "Language: Spanish" in text

    def test_empty_ciphertext_does_not_crash(self):
        text = report("", "en")
        assert "Total letters analyzed: 0" in text
