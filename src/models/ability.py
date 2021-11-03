
def get_attributes(rank_items) -> dict:
    attributes = {}
    for attribute in rank_items:
        attributes[attribute['description']] = attribute['value']
    return attributes


class Ability:
    name: str
    description: str
    url: str
    ident: int
    number: int
    cooldown: str
    cost: str
    attributes: dict

    def __init__(self, ability_dict: dict, number):
        self.name = ability_dict['Summary']
        self.description = ability_dict['Description']['itemDescription']['description']
        self.url = ability_dict['URL']
        self.ident = ability_dict['Id']
        self.number = number
        self.cooldown = ability_dict['Description']['itemDescription']['cooldown']
        self.cost = ability_dict['Description']['itemDescription']['cost']
        self.attributes = get_attributes(ability_dict['Description']['itemDescription']['rankitems'])
