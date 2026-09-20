from cyphers.caesar import decrypt as caesar_decrypt

# Source: https://es.sttmedia.com/frecuencias-de-letras-ingles
ENGLISH_FREQUENCY_TABLE = {
    'A': 0.0834, 'B': 0.0154, 'C': 0.0273, 'D': 0.0414, 'E': 0.1260,
    'F': 0.0203, 'G': 0.0192, 'H': 0.0611, 'I': 0.0671, 'J': 0.0023,
    'K': 0.0087, 'L': 0.0424, 'M': 0.0253, 'N': 0.0680, 'O': 0.0770,
    'P': 0.0166, 'Q': 0.0009, 'R': 0.0568, 'S': 0.0611, 'T': 0.0937,
    'U': 0.0285, 'V': 0.0106, 'W': 0.0234, 'X': 0.0020, 'Y': 0.0204,
    'Z': 0.0006
}

# Source: https://es.sttmedia.com/frecuencias-de-letras-espanol
SPANISH_FREQUENCY_TABLE = {
    'A': 0.1216, 'B': 0.0149, 'C': 0.0387, 'D': 0.0467, 'E': 0.1408,
    'F': 0.0069, 'G': 0.0100, 'H': 0.0118, 'I': 0.0598, 'J': 0.0052,
    'K': 0.0011, 'L': 0.0524, 'M': 0.0308, 'N': 0.0683, 'Ñ': 0.0017, 
    'O': 0.0920, 'P': 0.0289, 'Q': 0.0111, 'R': 0.0641, 'S': 0.0720, 
    'T': 0.0460, 'U': 0.0469, 'V': 0.0105, 'W': 0.0004, 'X': 0.0014, 
    'Y': 0.0109, 'Z': 0.0047
}

def chi_squared(text: str, table: dict[str, float]) -> float:
    observed_counts = {letter: 0 for letter in table.keys()}
    total_letters = 0

    for char in text.upper():
        if char in observed_counts:
            observed_counts[char] += 1
            total_letters += 1

    if total_letters == 0:
        return float('inf')

    chi_squared_stat = 0.0
    for letter, expected_freq in table.items():
        expected_count = expected_freq * total_letters
        if expected_count > 0:
            chi_squared_stat += ((observed_counts[letter] - expected_count) ** 2) / expected_count

    return chi_squared_stat / total_letters

def break_caesar(ciphertext: str, language: str = "en") -> tuple[int, str]:
    frequency_table = ENGLISH_FREQUENCY_TABLE if language == "en" else SPANISH_FREQUENCY_TABLE

    best_key = 0
    lowest_chi_squared = float('inf')
    best_plaintext = ""

    for key in range(26):
        plaintext = caesar_decrypt(ciphertext, key)
        chi_squared_value = chi_squared(plaintext, frequency_table)

        if chi_squared_value < lowest_chi_squared:
            lowest_chi_squared = chi_squared_value
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext
