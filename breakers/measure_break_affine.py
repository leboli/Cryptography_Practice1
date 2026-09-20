"""
Part C2 - measurement task for the Affine breaker.

For each fragment length, take 200 random fragments of a reference text,
encrypt each with a random key, run break_affine on it, and see how often
the recovered key matches the real one.

Run with:
    py -m breakers.measure_break_affine
"""
import random

from cyphers.affine import affine_encrypt
from breakers.break_affine import break_affine


# English: opening of "Pride and Prejudice" (Jane Austen) + the Gettysburg
# Address (Lincoln). Public domain.
ENGLISH_TEXT = """
It is a truth universally acknowledged, that a single man in possession
of a good fortune, must be in want of a wife. However little known the
feelings or views of such a man may be on his first entering a
neighbourhood, this truth is so well fixed in the minds of the
surrounding families, that he is considered as the rightful property of
some one or other of their daughters. My dear Mr Bennet, said his lady
to him one day, have you heard that Netherfield Park is let at last.
Mr Bennet replied that he had not. But it is, returned she, for Mrs Long
has just been here, and she told me all about it. Mr Bennet made no
answer. Do you not want to know who has taken it, cried his wife
impatiently. You want to tell me, and I have no objection to hearing it.
Four score and seven years ago our fathers brought forth on this
continent a new nation, conceived in liberty, and dedicated to the
proposition that all men are created equal. Now we are engaged in a
great civil war, testing whether that nation, or any nation so conceived
and so dedicated, can long endure. We are met on a great battlefield of
that war. We have come to dedicate a portion of that field, as a final
resting place for those who here gave their lives that that nation might
live. It is altogether fitting and proper that we should do this.
"""

# Spanish: opening of "Don Quijote de la Mancha" (Cervantes). Accents
# removed so every letter stays inside the A-Z range that caesar.py shifts.
# Public domain.
SPANISH_TEXT = """
En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha
mucho tiempo que vivia un hidalgo de los de lanza en astillero, adarga
antigua, rocin flaco y galgo corredor. Una olla de algo mas vaca que
carnero, salpicon las mas noches, duelos y quebrantos los sabados,
lantejas los viernes, algun palomino de anadidura los domingos,
consumian las tres partes de su hacienda. El resto della concluian sayo
de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo
mismo, y los dias de entresemana se honraba con su vellori de lo mas
fino. Tenia en su casa una ama que pasaba de los cuarenta, y una sobrina
que no llegaba a los veinte, y un mozo de campo y plaza, que asi
ensillaba el rocin como tomaba la podadera. En esto, descubrieron
treinta o cuarenta molinos de viento que hay en aquel campo, y asi como
don Quijote los vio, dijo a su escudero, la ventura va guiando nuestras
cosas mejor de lo que acertaramos a desear, porque ves alli, amigo
Sancho Panza, donde se descubren treinta, o pocos mas, desaforados
gigantes, con quien pienso hacer batalla.
"""

LENGTHS = [20, 30, 40, 60, 100]
TRIALS = 200

random.seed(42)  # reproducible results


def random_fragment(text: str, length: int) -> str:
    """Pick a random substring of text that contains exactly "length" letters."""
    letter_positions = [i for i, c in enumerate(text) if c.isalpha()]
    start = random.randrange(len(letter_positions) - length + 1)
    first = letter_positions[start]
    last = letter_positions[start + length - 1]
    return text[first:last + 1]


def recovery_rate(text: str, length: int, table: str) -> float:
    possible_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    correct = 0
    for _ in range(TRIALS):
        fragment = random_fragment(text, length)
        a = random.choice(possible_a)
        b = random.randrange(26)
        ciphertext = affine_encrypt(fragment, a, b)
        found_key, _ = break_affine(ciphertext, language=table)
        if found_key == (a, b):
            correct += 1
    return correct / TRIALS


if __name__ == "__main__":
    print(f"{'len':>4} {'EN/EN':>8} {'EN/ES':>8} {'ES/ES':>8} {'ES/EN':>8}")
    for length in LENGTHS:
        en_en = recovery_rate(ENGLISH_TEXT, length, "en")
        en_es = recovery_rate(ENGLISH_TEXT, length, "es")
        es_es = recovery_rate(SPANISH_TEXT, length, "es")
        es_en = recovery_rate(SPANISH_TEXT, length, "en")
        print(f"{length:>4} {en_en:>8.1%} {en_es:>8.1%} {es_es:>8.1%} {es_en:>8.1%}")
