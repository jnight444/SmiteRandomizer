from typing import Tuple

from src.models.ability import Ability
from src.models.enums import AttackRange, AttackType, Pantheon, Role


class God:

    name: str
    pantheon: Pantheon
    role: Role
    attack_type: AttackType
    attack_range: AttackRange
    title: str
    passive: Ability
    ability_1: Ability
    ability_1: Ability
    ability_1: Ability
    ultimate: Ability
    ident: int
    icon_url: str
    card_url: str

    def __init__(self, json: dict):
        self.name = json['Name']
        self.pantheon = Pantheon[json['Pantheon'].replace(' ', '_')]
        self.role = Role[json['Roles']]
        self.split_attack_info(json['Type'])
        self.title = json['Title']
        self.ability_1 = Ability(json['Ability_1'])
        self.ability_2 = Ability(json['Ability_2'])
        self.ability_3 = Ability(json['Ability_3'])
        self.ultimate = Ability(json['Ability_4'])
        self.passive = Ability(json['Ability_5'])
        self.ident = int(json['id'])
        self.icon_url = json['godIcon_URL']
        self.card_url = json['godCard_URL']

    def split_attack_info(self, data: str) -> None:
        type_list = data.split(',')

        if len(type_list) == 2:
            self.attack_range = AttackRange[type_list[0].strip()]
            self.attack_type = AttackType[type_list[1].strip()]
        else:
            self.attack_type = AttackType[type_list[0].strip()]

