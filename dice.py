from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


if __name__ == "__main__":
    my_die = Die()
    for _ in range(10):
        my_die.roll_die()
    print()
    my_die = Die(10)
    for _ in range(10):
        my_die.roll_die()
    print()
    my_die = Die(20)
    for _ in range(10):
        my_die.roll_die()
