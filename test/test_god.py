import unittest

from src.god import God
from src.enums import Role, Pantheon, AttackType, DamageType

param_list = [
    ({'role': 'role', 'pantheon': 'pantheon', 'attacktype': 'attacktype',
      'damagetype': 'damagetype', 'description': 'description'}),
    ({'name': 'name', 'pantheon': 'pantheon', 'attacktype': 'attacktype',
      'damagetype': 'damagetype', 'description': 'description'}),
    ({'name': 'name', 'role': 'role', 'attacktype': 'attacktype',
      'damagetype': 'damagetype', 'description': 'description'}),
    ({'name': 'name', 'role': 'role', 'pantheon': 'pantheon',
      'damagetype': 'damagetype', 'description': 'description'}),
    ({'name': 'name', 'role': 'role', 'pantheon': 'pantheon',
      'attacktype': 'pantheon', 'description': 'description'}),
    ({'name': 'name', 'role': 'role', 'pantheon': 'pantheon',
      'attacktype': 'pantheon', 'damagetype': 'damagetype'})
]


class GodTestSuite(unittest.TestCase):

    def test_constructor_missing_data(self):
        for data in param_list:
            with self.subTest():
                self.assertRaises(KeyError, God, **data)

    def test_constructor(self):
        god = God(**{'name': 'Test God',
                     'role': 'Mage',
                     'pantheon': 'Egyptian',
                     'attacktype': 'Ranged',
                     'damagetype': 'Physical',
                     'description': 'Testing constructor'}
                  )
        self.assertEqual(god.name, 'Test God')
        self.assertEqual(god.role, Role.Mage)
        self.assertEqual(god.pantheon, Pantheon.Egyptian)
        self.assertEqual(god.attacktype, AttackType.Ranged)
        self.assertEqual(god.damagetype, DamageType.Physical)
        self.assertEqual(god.description, 'Testing constructor')


if __name__ == '__main__':
    unittest.main()
