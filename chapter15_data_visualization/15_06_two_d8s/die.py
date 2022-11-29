from random import randint


# class that inits Die with optional num_sides as argument
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
