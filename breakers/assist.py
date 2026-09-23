from collections import Counter

from utils.constants import (
    ENGLISH_FREQUENCY_TABLE,
    SPANISH_FREQUENCY_TABLE,
    ENGLISH_BIGRAM_FREQUENCY_TABLE,
    ENGLISH_TRIGRAM_FREQUENCY_TABLE,
    SPANISH_BIGRAM_FREQUENCY_TABLE,
    SPANISH_TRIGRAM_FREQUENCY_TABLE,
)


def _language_tables(language: str) -> tuple[dict[str, float], dict[str, float], dict[str, float]]:
    if language == "es":
        return SPANISH_FREQUENCY_TABLE, SPANISH_BIGRAM_FREQUENCY_TABLE, SPANISH_TRIGRAM_FREQUENCY_TABLE
    return ENGLISH_FREQUENCY_TABLE, ENGLISH_BIGRAM_FREQUENCY_TABLE, ENGLISH_TRIGRAM_FREQUENCY_TABLE


def clean_letters(ciphertext: str, alphabet: set[str]) -> str:
    """Uppercase the ciphertext and drop anything that isn't a letter of the alphabet
    (spaces, punctuation, digits, unexpected characters are all discarded)."""
    return "".join(c for c in ciphertext.upper() if c in alphabet)


def ngrams(letters: str, n: int) -> list[str]:
    return [letters[i:i + n] for i in range(len(letters) - n + 1)]


def letter_frequencies(letters: str) -> list[tuple[str, int, float]]:
    """Ciphertext letters ranked by count, descending (ties broken alphabetically).
    Returns (letter, count, percentage) triples."""
    total = len(letters)
    counts = Counter(letters)
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [(letter, count, count / total * 100) for letter, count in ranked]


def repeated_ngrams(letters: str, n: int) -> dict[str, list[int]]:
    """n-grams that occur more than once, mapped to their 1-indexed start positions."""
    positions: dict[str, list[int]] = {}
    for i, gram in enumerate(ngrams(letters, n)):
        positions.setdefault(gram, []).append(i + 1)
    return {gram: pos for gram, pos in positions.items() if len(pos) > 1}


def top_bigrams(letters: str, n: int = 10) -> list[tuple[str, int, float]]:
    bigrams = ngrams(letters, 2)
    total = len(bigrams)
    counts = Counter(bigrams)
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    return [(bigram, count, count / total * 100 if total else 0.0) for bigram, count in ranked]


def doubled_letters(letters: str) -> dict[str, list[int]]:
    """Positions (1-indexed, start of the pair) of every doubled letter (e.g. 'TT')."""
    positions: dict[str, list[int]] = {}
    for i in range(len(letters) - 1):
        if letters[i] == letters[i + 1]:
            positions.setdefault(letters[i], []).append(i + 1)
    return positions


def suggested_mapping(letters: str, freq_table: dict[str, float]) -> dict[str, str]:
    """Align the ciphertext frequency ranking with the language frequency ranking,
    rank by rank, as a first guess. This is a starting point, not a solution:
    it ignores everything but single-letter frequency (bigrams, trigrams, doubles,
    word patterns), so it will misplace letters with close/tied frequencies."""
    cipher_ranked = [letter for letter, _, _ in letter_frequencies(letters)]
    plain_ranked = sorted(freq_table.keys(), key=lambda l: (-freq_table[l], l))
    return dict(zip(cipher_ranked, plain_ranked))


def report(ciphertext: str, language: str = "en") -> str:
    """Human-readable frequency analysis report for a monoalphabetic substitution
    cryptogram: letter frequencies vs. the expected language distribution, repeated
    trigrams with positions, the ten most frequent bigrams, doubled letters, and a
    suggested initial mapping from rank alignment. This does not solve the cipher;
    it does the bookkeeping a human solver would otherwise do by hand."""
    freq_table, bigram_table, trigram_table = _language_tables(language)
    alphabet = set(freq_table.keys())
    letters = clean_letters(ciphertext, alphabet)
    language_name = "Spanish" if language == "es" else "English"

    lines: list[str] = []
    lines.append("=" * 70)
    lines.append("FREQUENCY ASSISTANT REPORT")
    lines.append("=" * 70)
    lines.append(f"Language: {language_name}")
    lines.append(f"Total letters analyzed: {len(letters)}")
    lines.append(f"Distinct ciphertext letters: {len(set(letters))}")
    lines.append("")

    lines.append("-" * 70)
    lines.append(f"LETTER FREQUENCIES  (ciphertext, ranked)   vs   expected {language_name}")
    lines.append("-" * 70)
    lines.append(f"{'Rank':<5}{'Ltr':<5}{'Count':<7}{'%':<8}   {'Expect ltr':<12}{'Expect %':<8}")
    cipher_freqs = letter_frequencies(letters)
    plain_ranked = sorted(freq_table.items(), key=lambda kv: (-kv[1], kv[0]))
    for i in range(max(len(cipher_freqs), len(plain_ranked))):
        rank = i + 1
        if i < len(cipher_freqs):
            c_letter, c_count, c_pct = cipher_freqs[i]
            cipher_part = f"{c_letter:<5}{c_count:<7}{c_pct:<8.2f}"
        else:
            cipher_part = f"{'':<5}{'':<7}{'':<8}"
        if i < len(plain_ranked):
            p_letter, p_freq = plain_ranked[i]
            plain_part = f"{p_letter:<12}{p_freq * 100:<8.2f}"
        else:
            plain_part = ""
        lines.append(f"{rank:<5}{cipher_part}   {plain_part}")
    lines.append("")

    lines.append("-" * 70)
    lines.append("REPEATED TRIGRAMS  (ciphertext trigrams that occur more than once)")
    lines.append("-" * 70)
    repeated_tri = repeated_ngrams(letters, 3)
    if repeated_tri:
        for tg, positions in sorted(repeated_tri.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            lines.append(f"{tg}: count={len(positions)}, positions={positions}")
    else:
        lines.append("(none)")
    lines.append("")
    top_trigrams = sorted(trigram_table.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
    lines.append(f"For reference, top {language_name} trigrams: " +
                 ", ".join(f"{tg} ({freq * 100:.2f}%)" for tg, freq in top_trigrams))
    lines.append("")

    lines.append("-" * 70)
    lines.append("TOP 10 MOST FREQUENT BIGRAMS  (ciphertext)")
    lines.append("-" * 70)
    for bg, count, pct in top_bigrams(letters, 10):
        lines.append(f"{bg}: count={count}, {pct:.2f}%")
    lines.append("")
    top_language_bigrams = sorted(bigram_table.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
    lines.append(f"For reference, top {language_name} bigrams: " +
                 ", ".join(f"{bg} ({freq * 100:.2f}%)" for bg, freq in top_language_bigrams))
    lines.append("")

    lines.append("-" * 70)
    lines.append("DOUBLED LETTERS  (ciphertext)")
    lines.append("-" * 70)
    doubles = doubled_letters(letters)
    if doubles:
        for letter, positions in sorted(doubles.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            lines.append(f"{letter}{letter}: count={len(positions)}, positions={positions}")
    else:
        lines.append("(none)")
    lines.append("")

    lines.append("-" * 70)
    lines.append("SUGGESTED INITIAL MAPPING  (rank alignment: cipher letter -> plaintext guess)")
    lines.append("-" * 70)
    mapping = suggested_mapping(letters, freq_table)
    for cipher_letter, plain_letter in sorted(mapping.items()):
        lines.append(f"{cipher_letter} -> {plain_letter}")
    lines.append("")
    lines.append("This mapping is a starting point only, based purely on frequency rank.")
    lines.append("Cross-check it against the bigrams, trigrams and doubled letters above,")
    lines.append("and against common short words, before trusting any single letter.")

    return "\n".join(lines)
