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

# Source: https://en.wikipedia.org/wiki/Bigram
ENGLISH_BIGRAM_FREQUENCY_TABLE = {
    'TH': 0.0271, 'HE': 0.0233, 'IN': 0.0203, 'ER': 0.0178, 'AN': 0.0161,
    'RE': 0.0141, 'ES': 0.0132, 'ON': 0.0132, 'ST': 0.0125, 'NT': 0.0117,
    'EN': 0.0113, 'AT': 0.0112, 'ED': 0.0108, 'ND': 0.0107, 'TO': 0.0107,
    'OR': 0.0106, 'EA': 0.0100, 'TI': 0.0099, 'AR': 0.0098, 'TE': 0.0098,
    'NG': 0.0089, 'AL': 0.0088, 'IT': 0.0088, 'AS': 0.0087, 'IS': 0.0086,
    'HA': 0.0083, 'ET': 0.0076, 'SE': 0.0073, 'OU': 0.0072, 'OF': 0.0071,
}

# Source: https://en.wikipedia.org/wiki/Trigram
ENGLISH_TRIGRAM_FREQUENCY_TABLE = {
    'THE': 0.0181, 'AND': 0.0073, 'ING': 0.0072, 'ENT': 0.0042, 'ION': 0.0042,
    'HER': 0.0036, 'FOR': 0.0034, 'THA': 0.0033, 'NTH': 0.0033, 'INT': 0.0032,
    'ERE': 0.0031, 'TIO': 0.0031, 'TER': 0.0030, 'EST': 0.0028, 'ERS': 0.0028,
    'ATI': 0.0026, 'HAT': 0.0026, 'ATE': 0.0025, 'ALL': 0.0025, 'ETH': 0.0024,
    'HES': 0.0024, 'VER': 0.0024, 'HIS': 0.0024, 'OFT': 0.0022, 'ITH': 0.0021,
    'FTH': 0.0021, 'STH': 0.0021, 'OTH': 0.0021, 'RES': 0.0021, 'ONT': 0.0020,
}

# Source: https://elladodelmal.com
SPANISH_BIGRAM_FREQUENCY_TABLE = {
    'EN': 0.0301, 'DE': 0.0277, 'ER': 0.0225, 'ES': 0.0220, 'UE': 0.0203,
    'LA': 0.0191, 'RA': 0.0183, 'OS': 0.0173, 'NT': 0.0168, 'TE': 0.0155,
    'AR': 0.0154, 'QU': 0.0144, 'EL': 0.0140, 'TA': 0.0138, 'DO': 0.0135,
    'CO': 0.0131, 'RE': 0.0129, 'AS': 0.0128, 'ON': 0.0115, 'AN': 0.0115,
    'TO': 0.0111, 'LO': 0.0110, 'ST': 0.0109, 'UN': 0.0107, 'OR': 0.0104,
    'AD': 0.0102, 'IE': 0.0101, 'SE': 0.0099, 'CI': 0.0098, 'AL': 0.0091,
    'PA': 0.0088, 'NA': 0.0088, 'RO': 0.0085, 'NO': 0.0082, 'ME': 0.0080,
    'IN': 0.0077,
}

# Same source as the bigrams, without accents.
SPANISH_TRIGRAM_FREQUENCY_TABLE = {
    'QUE': 0.0166, 'ENT': 0.0138, 'NTE': 0.0107, 'CON': 0.0085, 'EST': 0.0083,
    'ADO': 0.0071, 'PAR': 0.0069, 'LOS': 0.0067, 'ERA': 0.0064, 'IEN': 0.0061,
    'MEN': 0.0060, 'PER': 0.0053, 'STA': 0.0050, 'ARA': 0.0050, 'POR': 0.0047,
    'UNA': 0.0047, 'ION': 0.0046, 'ANT': 0.0045, 'TRA': 0.0045, 'ERO': 0.0044,
    'NTO': 0.0044, 'CIO': 0.0039, 'ACI': 0.0038, 'LAS': 0.0037, 'COM': 0.0037,
    'STE': 0.0036, 'RES': 0.0035, 'IER': 0.0034, 'TEN': 0.0034, 'DOS': 0.0033,
    'DES': 0.0033, 'VER': 0.0033, 'IDO': 0.0030, 'ADA': 0.0030,
}

# Pride and Prejudice (start) + Gettysburg Address
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

# Don Quijote (start), without accents
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
