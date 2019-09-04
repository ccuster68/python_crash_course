from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides=sides

    def roll_die(self):
        print(randint(1,self.sides))

# Test        
die=Die(10)
for n in range(1,21):
    die.roll_die()
