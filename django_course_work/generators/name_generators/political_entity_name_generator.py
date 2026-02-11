import random

ADJECTIVES = [
    "Golden",
    "Silver",
    "Crimson",
    "Azure",
    "Emerald",
    "Ivory",
    "Obsidian",
    "Radiant",
    "Sacred",
    "Iron",
    "Storm",
    "Silent",
    "Hidden",
    "Shattered",
    "Eternal",
    "Fallen",
    "Rising",
    "Ancient",
    "New",
    "Grand",
    "Free",
    "United",
    "Northern",
    "Southern",
    "Eastern",
    "Western",
    "Verdant",
    "Burning",
    "Frozen",
    "Luminous",
]


NOUNS = [
    "Empire",
    "Kingdom",
    "Dominion",
    "Republic",
    "Federation",
    "Confederacy",
    "Alliance",
    "Coalition",
    "Union",
    "League",
    "Order",
    "Covenant",
    "Dynasty",
    "Throne",
    "Crown",
    "Principality",
    "Realm",
    "Marches",
    "Territories",
    "Clans",
    "Tribes",
    "Collective",
    "Assembly",
    "Council",
    "Protectorate",
    "Enclave",
    "States",
    "Hegemony",
    "Syndicate",
    "Compact",
]



def generate_name_for_political_entity(seed: float | None = None) -> str:
    rng = random.Random(seed)

    adjective = rng.choice(ADJECTIVES)
    noun = rng.choice(NOUNS)

    return f"{adjective} {noun}"
