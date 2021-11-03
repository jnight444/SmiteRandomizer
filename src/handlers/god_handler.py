import json
from random import choice
from typing import List

from src.models.god import God


class GodHandler:
    god_list: List[God] = []

    def __init__(self):
        # Read in all god data and parse into God objects
        for god in json.load(open('../../data/gods.json')):
            self.god_list.append(God(god))

    def get_god(self, god_name: str) -> God:
        return next((g for g in self.god_list if g.name == god_name), None)

    def get_random_god(self) -> God:
        return choice(self.god_list)
