from typing import List

from src.models.enums import ItemType, Role


class Item:
    name: str
    description: str
    url: str
    tier: int
    price: int
    ident: int
    childIdent: int
    is_active: bool
    is_starter: bool
    type: ItemType
    roles: List[Role]
    attributes: dict

    def __init__(self, json):
        self.name = json['DeviceName']
        self.description = json['ItemDescription']['Description']
        self.url = json['itemIcon_URL']
        self.tier = int(json['ItemTier'])
        self.price = int(json['Price'])
        self.ident = int(json['ItemId'])
        self.childIdent = int(json['ChildItemId'])
        self.is_active = json['ActiveFlag'] == 'y'
        self.is_starter = json['StartingItem']
        self.type = ItemType[json['Type']]
        self.roles = self.get_roles(json['RestrictedRoles'])
        self.attributes = self.get_attributes(json['ItemDescription']['Menuitems'])

    @staticmethod
    def get_roles(roles_str: str) -> List[Role]:
        roles = []
        role_list = roles_str.split(',')
        for role in role_list:
            try:
                roles.append(Role[role.capitalize()])
            except KeyError:
                roles += [role for role in Role]
        return roles

    @staticmethod
    def get_attributes(menu_items: dict) -> dict:
        attributes: dict = {}
        for entry in menu_items:
            attributes[entry['Description']] = entry['Value']
        return attributes
