from random import randint, choice


class Die:
    def __init__(self, number_of_sides=6):
        self.number_of_sides = number_of_sides

    def roll_die(self):
        return randint(1, self.number_of_sides)


die_6 = Die()
roll_times = 20
print(f"Rolling die {roll_times}.")
[print(f"{i+1}:{die_6.roll_die()}", end=', ') for i in range(roll_times)]
print("\n")

roll_times = 10

die = Die(10)
print(f"Rolling die {die.number_of_sides} {roll_times} times")
[print(f"{i +1}:{die.roll_die()}", end=' ') for i in range(roll_times)]
print()

die = Die(20)
print(f"Rolling die {die.number_of_sides} {roll_times} times")
[print(f"{i +1}:{die.roll_die()}", end=' ') for i in range(roll_times)]
print()

