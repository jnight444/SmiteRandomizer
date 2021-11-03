import json
from random import choice, sample
from typing import List
from src.models.enums import AttackType, ItemType
from src.models.god import God
from src.models.item import Item


def get_all_items() -> List[Item]:
    return [Item(item) for item in json.load(open('../../data/items.json'))]


def get_all_active_items() -> List[Item]:
    return [item for item in get_all_items() if
            item.is_active and
            "Scare Tactics" not in item.name]


def filter_specific_god_cases(god, item_list):
    if 'Baron' not in god.name:
        item_list = [i for i in item_list if 'Baron' not in i.name]
    if 'Ratatoskr' not in god.name:
        item_list = [i for i in item_list if 'Acorn' not in i.name]
    return item_list


class ItemHandler:
    item_list: List[Item] = []

    def __init__(self):
        self.item_list = get_all_active_items()

    def get_item_by_name(self, item_name: str) -> Item:
        return next((i for i in self.item_list if i.name == item_name), None)

    def get_item_by_id(self, ident: int) -> Item:
        return next((i for i in self.item_list if i.ident == ident), None)

    def get_filtered_item_list(self,
                               god: God = None,
                               tier: int = None,
                               starter: bool = None,
                               item_type: ItemType = None) -> List[Item]:
        item_list = self.item_list

        # Filter based on the given god
        if god is not None:
            item_list = [item for item in item_list if god.role in item.roles]
            item_list = filter_specific_god_cases(god, item_list)

            if item_type is not None and item_type == ItemType.Item:
                item_list = [item for item in item_list if
                             god.attack_type == item.attack_type or
                             item.attack_type == AttackType.Any]

        if tier is not None:
            item_list = [item for item in item_list if item.tier == tier]
        if starter is not None:
            item_list = [item for item in item_list if item.is_starter == starter]
        if item_type is not None:
            item_list = [item for item in item_list if item.type == item_type]

        return item_list

    def get_random_starter(self) -> Item:
        return choice(self.get_filtered_item_list(starter=True, tier=2, item_type=ItemType.Item))

    def get_random_items(self, god: God) -> List[Item]:
        return sample(self.get_filtered_item_list(god=god, tier=3, item_type=ItemType.Item), 5)

    def get_random_relics(self) -> List[Item]:
        return sample(self.get_filtered_item_list(item_type=ItemType.Active, tier=2), 2)

    def get_random_consumables(self, god: God) -> List[Item]:
        return sample(self.get_filtered_item_list(item_type=ItemType.Consumable, god=god), 2)
