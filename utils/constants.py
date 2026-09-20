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
