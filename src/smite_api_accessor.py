import json


from pyrez.api.SmiteAPI import SmiteAPI

from src import keys

session_id = '1802F16D0CC04561B8D9A758C2BD12B7'

smite = SmiteAPI(keys.dev_id, keys.auth_key, sessionId=session_id)


def get_gods():
    gods = [god.json for god in smite.getGods()]

    with open('../data/gods.json', 'w') as outfile:
        json.dump(gods, outfile, indent=10)


def get_items():
    items = [item.json for item in smite.getItems()]
    print(items)

    # with open('../data/items.json', 'w') as outfile:
    #     json.dump(items, outfile, indent=15)


if __name__ == '__main__':
    print(smite.getItems())
