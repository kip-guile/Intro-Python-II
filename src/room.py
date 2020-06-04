# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None
        self.items = items

    # def __str__(self):
    #     return f'This room is called {self.name} and it is described as {self.description}'

    def where(self):
        print(f'You are in {self.name}.\n {self.description}')

    def environment(self):
        if len(self.items) < 1:
            pass
        else:
            print(f'\nItems available in {self.name}:')
            for i in self.items:
                print(i)
