from world_building.models import PoliticalEntity
from generators.name_generators.political_entity_name_generator import generate_name_for_political_entity
import random

GOVERNMENT_TYPES = [
    "Monarchy",
    "Absolute Monarchy",
    "Constitutional Monarchy",
    "Empire",
    "Theocracy",
    "Republic",
    "Democracy",
    "Federation",
    "Confederation",
    "Tribal Council",
    "Clan Alliance",
    "Merchant Guild",
    "Trade League",
    "Oligarchy",
    "Magocracy",
    "Military Junta",
    "Technocracy",
    "Aristocracy",
    "City-State",
    "Nomadic Horde",
    "Sacred Order",
    "Corporate State",
    "Collective",
    "Council State",
    "Dynastic Rule",
]


PERSONALITY_TYPES = [
    "Militaristic",
    "Expansionist",
    "Isolationist",
    "Diplomatic",
    "Zealous",
    "Scholarly",
    "Industrial",
    "Merchant-minded",
    "Traditionalist",
    "Reformist",
    "Decadent",
    "Ascetic",
    "Honor-bound",
    "Secretive",
    "Xenophobic",
    "Xenophilic",
    "Innovative",
    "Stoic",
    "Opportunistic",
    "Fanatical",
    "Pacifist",
    "Exploitative",
    "Spiritual",
    "Pragmatic",
    "Idealistic",
]



def generate_political_entities(world, count=10):
    for _ in range(count):
        PoliticalEntity.objects.create(
            world=world,
            name=generate_name_for_political_entity(),
            government_type=random.choice(GOVERNMENT_TYPES),
            dominant_trait=random.choice(PERSONALITY_TYPES),
            power_level=random.randint(30, 90),
        )

