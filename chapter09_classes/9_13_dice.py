import random

# dice class 
class Dice():
    def __init__(self):
        self.sides = 6
    # method to roll dice
    def roll_dice(self):
        print(f"\tRolling {self.sides} sided dice!")
        # random side from 1 to self.sides
        result = random.randint(1, self.sides)
        print(f"\tResult is {result}!\n")

# make instances 
normal_dice = Dice()

ten_sided_dice = Dice()
ten_sided_dice.sides = 10

twenty_sided_dice = Dice()
twenty_sided_dice.sides = 20

# roll each 10 times
rolls = range(0, 10)
for roll in rolls:
    normal_dice.roll_dice()
    ten_sided_dice.roll_dice()
    twenty_sided_dice.roll_dice()