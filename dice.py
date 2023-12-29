from random import randint

class Dice:
    def __init__(self, sides=10):
        self.sides = sides

    def roll_die(self):
        random_number = randint(1, self.sides)
        print(random_number)


dice = Dice()

dice.roll_die()
dice.roll_die()
dice.roll_die()