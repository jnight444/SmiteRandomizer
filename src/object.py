
class Object:
    name: str
    cost: int
    description: str

    def __init__(self, name: str, cost: int, description: str):
        self.name = name
        self.cost = cost
        self.description = description

    def print(self):
        print(f'Name: {self.name}')
        print(f'Cost: {self.cost}')
        print(f'Description: {self.description}')
