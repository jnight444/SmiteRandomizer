from old_code.src.object import Object


class Item(Object):

    constant_attributes = [
        'physical_power',
        'magical_power',
        'physical_protection',
        'magical_protection',
        'health',
        'hp5'
    ]
    percent_attributes = [
        'attack_speed',
        'physical_lifesteal',
        'magical_lifesteal',
        'physical_penetration',
        'magical_penetration',
        'crit_chance',
        'ccr',
        'movement_speed',
        'cooldown',
        'mana',
        'mp5',
    ]

    attribute_list = constant_attributes + percent_attributes

    def __init__(self, name: str, cost: int, description: str, attr: str):
        super(Item, self).__init__(name, cost, description)

        self.attributes = {}
        self.get_attributes(attr)

    def get_attributes(self, attribute_string: str) -> None:
        attribute_list = attribute_string.split(';')

        for attribute in attribute_list:
            key_value = attribute.split(':')
            key = key_value[0]
            value = key_value[1]

            if key in self.attribute_list:
                self.attributes[key] = value

    def print(self):
        print(f'Name: {self.name}')
        print(f'Cost: {self.cost}')
        print(f'Description: {self.description}')

        filtered_attributes = [(k, v) for (k, v) in self.attributes.items()
                               if v is not None]

        if filtered_attributes:
            print('Attributes:')
            for k, v in filtered_attributes:
                print(f' - {self.make_pretty(k)}: {v}' +
                      ('%' if k in self.percent_attributes else ''))

    @staticmethod
    def make_pretty(s: str) -> str:
        if len(s) <= 3:
            return s.upper()

        return " ".join([word.capitalize() for word in s.split('_')])
