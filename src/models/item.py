from typing import List

from src.models.enums import ItemType, Role


class Item:
    name: str
    description: str
    url: str
    tier: int
    price: int
    ident: int
    is_active: bool
    is_starter: bool
    type: ItemType
    roles: List[Role] = []
    attributes: dict = {}

    def __init__(self, json):
        self.name = json['DeviceName']
        self.description = json['ItemDescription']['Description']
        self.url = json['itemIcon_URL']
        self.tier = int(json['ItemTier'])
        self.price = int(json['Price'])
        self.ident = int(json['ItemId'])
        self.is_active = json['ActiveFlag'] == 'y'
        self.is_starter = json['StartingItem']
        self.type = ItemType[json['Type']]
        self.attributes = self.get_attributes(json['ItemDescription']['Menuitems'])

    def get_roles(self, roles_str):
        pass

    def get_attributes(self, menu_items: dict) -> dict:
        pass
