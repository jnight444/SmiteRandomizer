import json


from pyrez.api.SmiteAPI import SmiteAPI

dev_id = '4104'
auth_key = ''
session_id = ''
my_player_id = '709261308'

smite = SmiteAPI(dev_id, auth_key, sessionId=session_id)


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
