# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current):
        self.current = current
        self.name = name

    # def __str__(self):
    #     return f'Current room {self.current}'

    def move(self, direction):
        if getattr(self.current, f'{direction}_to') == None:
            print(f'You cant move there, change direction')
        elif getattr(self.current, f'{direction}_to') != None:
            setattr(self, 'current', getattr(self.current, f'{direction}_to'))
            self.current.where()
