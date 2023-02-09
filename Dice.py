import random

class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.value = random.randint(1, self.sides)
				
    def __str__(self):
        return f'Sidor: {self.sides:2d}, värde: {self.value:2d}'    

    def roll(self):
        self.value = random.randint(1, self.sides) 

n = int(input('Insätt antalet gånger du vill slå tärningen n: '))

class PokerDice:
    def __init__(self):
        self.dice_list = []
        for i in range(n):
            self.dice_list.append(Dice(6))

    def __str__(self):
        return str(sorted([d.value for d in self.dice_list])) 

    def roll(self):
        for d in self.dice_list:
            d.roll()      # Använder rollmetoden i Dice

    def number_of_dices(self):
        return len(self.dice_list)

print('Pokertärningar:')
pd = PokerDice()
for i in range(10):
    pd.roll()
    print(pd)