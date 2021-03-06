from typing import List

from src.ability_handler import AbilityHandler
from src.handlers.god_handler import GodHandler
from src.handlers.item_handler import ItemHandler
from src.models.ability import Ability
from src.models.god import God
from src.models.item import Item

END_LINE = '\n'


class RandomBuild:

    god_handler = GodHandler()
    item_handler = ItemHandler()

    god: God
    starter: Item
    items: List[Item]
    relics: List[Item]
    consumables: List[Item]
    abilities: List[Ability]

    def __init__(self):
        self.god = self.god_handler.get_random_god()
        self.starter = self.item_handler.get_random_starter()
        self.items = self.item_handler.get_random_items(god=self.god)
        self.relics = self.item_handler.get_random_relics()
        self.consumables = self.item_handler.get_random_consumables(god=self.god)
        self.abilities = AbilityHandler(self.god).get_abilities()

    def print_build(self):
        print(self.get_build_string())

    def get_build_string(self) -> str:
        build_string = ''
        build_string += 'God:' + END_LINE
        build_string += self.god.name + END_LINE

        build_string += 'Items:' + END_LINE
        build_string += f' - {self.starter.name}' + END_LINE
        for item in self.items:
            build_string += f' - {item.name}' + END_LINE

        build_string += 'Relics:' + END_LINE
        for relic in self.relics:
            build_string += f' - {relic.name}' + END_LINE

        build_string += 'Consumables:' + END_LINE
        for consumable in self.consumables:
            build_string += f' - {consumable.name}' + END_LINE
        return build_string

    def get_abilitiy_order(self) -> List[Ability]:
        abilities: List[Ability] = []
        player_level: int = 1



        return None


if __name__ == '__main__':
    build = RandomBuild()
    build.print_build()
