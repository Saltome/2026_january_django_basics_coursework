import random

ADJECTIVES = [
    "Ashen", "Golden", "Silent", "Crimson", "Forgotten",
    "Eternal", "Shattered", "Verdant", "Umbral",
]

NOUNS = [
    "Realm", "World", "Kingdom", "Plane", "Dominion",
    "Vale", "Sphere", "Lands",
]


def generate_world_name(seed: float | None = None) -> str:
    rng = random.Random(seed)

    adjective = rng.choice(ADJECTIVES)
    noun = rng.choice(NOUNS)

    return f"{adjective} {noun}"
