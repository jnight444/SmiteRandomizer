import random
from typing import List

from src.god_handler import GodHandler
from src.models.ability import Ability
from src.models.god import God


class AbilityHandler:
    god: God
    player_level: int = 1
    ability1_level: int = 0
    ability2_level: int = 0
    ability3_level: int = 0
    ult_level: int = 0

    abilities = []

    ability_upgrade_requirements = {
        1: 1,
        2: 3,
        3: 5,
        4: 7,
        5: 9
    }

    ultimate_upgrade_requirements = {
        1: 5,
        2: 9,
        3: 13,
        4: 17,
        5: 20
    }

    def __init__(self, god: God):
        self.god = god
        self.abilities = []

    def get_abilities(self):

        while len(self.abilities) < 20:
            random_num = random.randint(1, 4)

            if random_num == 1 and self.can_upgrade_ability(self.ability1_level + 1):
                self.ability1_level += 1
                self.player_level += 1
                self.abilities.append(self.god.ability_1)
            elif random_num == 2 and self.can_upgrade_ability(self.ability2_level + 1):
                self.ability2_level += 1
                self.player_level += 1
                self.abilities.append(self.god.ability_2)
            elif random_num == 3 and self.can_upgrade_ability(self.ability3_level + 1):
                self.ability3_level += 1
                self.player_level += 1
                self.abilities.append(self.god.ability_3)
            elif random_num == 4 and self.can_upgrade_ultimate():
                self.ult_level += 1
                self.player_level += 1
                self.abilities.append(self.god.ultimate)

        return self.abilities

    def can_upgrade_ability(self, ability_level) -> bool:
        if ability_level > 5:
            return False
        return self.player_level >= self.ability_upgrade_requirements[ability_level]

    def can_upgrade_ultimate(self) -> bool:
        if self.ult_level + 1 > 5:
            return False
        return self.player_level >= self.ultimate_upgrade_requirements[self.ult_level + 1]


if __name__ == '__main__':
    ability_handler = AbilityHandler(GodHandler().get_god('Ymir'))
    print(ability_handler.get_abilities())


