# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current):
        self.current = current
        self.name = name
        self.inventory = []

    # def __str__(self):
    #     return f'Current room {self.current}'

    def move(self, direction):
        if getattr(self.current, f'{direction}_to') == None:
            print(f'You cant move there, change direction')
        elif getattr(self.current, f'{direction}_to') != None:
            setattr(self, 'current', getattr(self.current, f'{direction}_to'))
            self.current.where()
            self.current.environment()

    def pick_up(self, item):
        if item in self.current.items:
            self.inventory.append(item)
            self.current.items.remove(item)
            print(f'inventory: {self.inventory}')

    def drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current.items.append(item)
            print(f'inventory: {self.inventory}')
