from enum import Enum, auto


class Pantheon(Enum):
    Arthurian = auto()
    Babylonian = auto()
    Chinese = auto()
    Celtic = auto()
    Egyptian = auto()
    Greek = auto()
    Great_Old_Ones = auto()
    Hindu = auto()
    Japanese = auto()
    Maya = auto()
    Norse = auto()
    Polynesian = auto()
    Roman = auto()
    Slavic = auto()
    Voodoo = auto()
    Yoruba = auto()


class Role(Enum):
    Guardian = auto()
    Warrior = auto()
    Hunter = auto()
    Mage = auto()
    Assassin = auto()


class AttackType(Enum):
    Magical = auto()
    Physical = auto()


class AttackRange(Enum):
    Ranged = auto()
    Melee = auto()


class ItemType(Enum):
    Item = auto()
    Active = auto()
    Consumable = auto()
