# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.room = room
        self.name = name

    def __str__(self):
        return f'Current room {self.room}'
