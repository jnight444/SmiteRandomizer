from old_code.src.enums import Role, Pantheon, AttackType, DamageType


class God:
    name: str
    role: Role
    pantheon: Pantheon
    attacktype: AttackType
    damagetype: DamageType
    description: str

    def __init__(self, **data):
        self.name = data['name']
        self.role = Role[data['role']]
        self.pantheon = Pantheon[data['pantheon']]
        self.attacktype = AttackType[data['attacktype']]
        self.damagetype = DamageType[data['damagetype']]
        self.description = data['description']

    def print(self):
        print(f'Name: {self.name}')
        print(f'Role: {self.role.name}')
        print(f'Pantheon: {self.pantheon.name}')
        print(f'Attack Type: {self.attacktype.name}')
        print(f'Damage Type: {self.damagetype.name}')
        print(f'Description: {self.description}')
