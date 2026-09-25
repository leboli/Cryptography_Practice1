import random

from utils.basics import normalise


def random_fragments(text: str, length: int, count: int = 20, seed: int = 0) -> list[str]:
    # `count` random pieces of the normalised text, each exactly `length` letters long
    rng = random.Random(seed)
    letters = normalise(text)
    starts = [rng.randrange(len(letters) - length + 1) for _ in range(count)]
    return [letters[s:s + length] for s in starts]
