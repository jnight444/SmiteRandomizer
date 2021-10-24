import csv
from typing import List

from old_code.src.consumable import Consumable
from old_code.src.god import God
from old_code.src.item import Item
from old_code.src.relic import Relic


class CSVReader:

    # Default csv files
    GOD_FILE = '../old_data/gods.csv'
    ITEM_FILE = '../old_data/items.csv'
    CONSUMABLE_FILE = '../old_data/consumables.csv'
    RELIC_FILE = '../old_data/relics.csv'

    def __init__(self,
                 god_file=GOD_FILE,
                 item_file=ITEM_FILE,
                 consumable_file=CONSUMABLE_FILE,
                 relic_file=RELIC_FILE):

        self.god_reader = csv.DictReader(open(god_file))
        self.item_reader = csv.DictReader(open(item_file))
        self.consumable_reader = csv.DictReader(open(consumable_file))
        self.relic_reader = csv.DictReader(open(relic_file))

    def get_god_list(self) -> List[God]:
        return [God(**god) for god in self.god_reader]

    def get_item_list(self) -> List[Item]:
        return [
            Item(
                item['name'],
                item['cost'],
                item['description'],
                item['attributes']
            )
            for item in self.item_reader
        ]

    def get_consumable_list(self) -> List[Consumable]:
        return [
            Consumable(
                con['name'],
                con['cost'],
                con['description']
            )
            for con in self.consumable_reader
        ]

    def get_relic_list(self):
        return [
            Relic(
                relic['name'],
                relic['cooldown'],
                relic['description']
            )
            for relic in self.relic_reader
        ]


if __name__ == '__main__':
    reader = CSVReader()
    for thing in reader.get_item_list():
        thing.print()
        print()
