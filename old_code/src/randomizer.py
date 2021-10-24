import random
from typing import List

from old_code.src.consumable import Consumable
from old_code.src.csv_reader import CSVReader
from old_code.src.god import God
from old_code.src.item import Item
from old_code.src.relic import Relic


class Randomizer:

    def __init__(self):
        self.reader = CSVReader()

    def get_random_god(self) -> God:
        return random.choice(self.reader.get_god_list())

    def get_random_items(self) -> List[Item]:
        return random.sample(self.reader.get_item_list(), 6)

    def get_random_relics(self) -> List[Relic]:
        return random.sample(self.reader.get_relic_list(), 2)

    def get_random_consumables(self) -> List[Consumable]:
        return random.sample(self.reader.get_consumable_list(), 2)


if __name__ == '__main__':
    randomizer = Randomizer()
    print("God:")
    print(randomizer.get_random_god().name)

    print("\nItems:")
    for item in randomizer.get_random_items():
        print(f' - {item.name} - {item.cost}')

    print("\nRelics:")
    for relic in randomizer.get_random_relics():
        print(f' - {relic.name}')

    print("\nConsumables:")
    for consumable in randomizer.get_random_consumables():
        print(f' - {consumable.name} - {consumable.cost}')
