import enum


class Role(enum.Enum):
    Guardian = 1
    Warrior = 2
    Hunter = 3
    Mage = 4
    Assassin = 5


class Pantheon(enum.Enum):
    Arthurian = 1
    Babylonian = 2
    Chinese = 3
    Celtic = 4
    Egyptian = 5
    Greek = 6
    Great_Old_Ones = 6
    Hindu = 8
    Japanese = 9
    Maya = 10
    Norse = 11
    Polynesian = 12
    Roman = 13
    Slavic = 14
    Voodoo = 15
    Yoruba = 16


class AttackType(enum.Enum):
    Melee = 1
    Ranged = 2


class DamageType(enum.Enum):
    Magical = 1
    Physical = 2
