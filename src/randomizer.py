import json
from typing import List, Tuple

from random import choice, sample
from src.models.enums import ItemType, Role
from src.models.god import God
from src.models.item import Item


def get_random_starter_items() -> Tuple[Item, Item]:
    starter_evolved = choice([i for i in items if i.is_starter and i.tier == 2])
    starter = next((i for i in items if i.ident == starter_evolved.childIdent), None)
    return starter, starter_evolved


def get_random_items(role: Role) -> List[Item]:
    sample_set = [i for i in items if
                  i.type == ItemType.Item and
                  i.tier == 3 and
                  i.is_active and
                  role in i.roles]
    return sample(sample_set, 5)


def get_random_relics() -> List[Item]:
    return sample([i for i in items if i.type is ItemType.Active and i.tier == 2], 2)


def get_random_consumables() -> List[Item]:
    return sample([i for i in items if i.type is ItemType.Consumable], 2)


def filter_items_by_active() -> List[Item]:
    return [i for i in items if i.is_active]


# Create lists to hold our data
gods: List[God] = []
items: List[Item] = []

# Read in all god data and parse into God objects
for god in json.load(open('../data/gods.json')):
    gods.append(God(god))

# Read in all item data and parse into Item objects
for item in json.load(open('../data/items.json')):
    items.append(Item(item))

# Filter items by active
items = filter_items_by_active()

god = choice(gods)
starters = get_random_starter_items()

print(f'God:\n{god.name}')
print()
print(f'Items:\n{starters[0].name} -> {starters[1].name}')
for item in get_random_items(god.role):
    print(f'{item.name} : {item.attributes}')

print()
print("Relics:")
for relic in get_random_relics():
    print(relic.name)

print()
print("Consumables:")
for consumable in get_random_consumables():
    print(consumable.name)
