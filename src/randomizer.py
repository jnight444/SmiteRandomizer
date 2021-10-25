import json
from typing import List

from src.models.god import God
from src.models.item import Item

gods_json = json.load(open('../data/gods.json'))
items_json = json.load(open('../data/items.json'))

gods: List[God] = []
items: List[Item] = []
types: set = set()

for god in gods_json:
    gods.append(God(god))

for item in items_json:
    types.add(item['Type'])
    items.append(Item(item))

for item in items:
    print(item.__dict__)

print(types)
