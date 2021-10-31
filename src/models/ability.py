

class Ability:
    name: str
    description: str
    url: str
    ident: int
    number: int

    def __init__(self, ability_dict: dict, number):
        self.name = ability_dict['Summary']
        self.description = ability_dict['Description']
        self.url = ability_dict['URL']
        self.ident = ability_dict['Id']
        self.number = number
