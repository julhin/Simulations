import random as rnd

class Dice:

    def __init__(self, sides = 6):
        self.sides = sides
        self.seed = rnd.seed()

    def roll_dice(self, rolls = 1):
        results = []
        for i in range(0, rolls):
            results.append(rnd.randint(1, self.sides)) 
        results.sort()
        return results

if __name__ == "__main__":
    dice = Dice()
    print(dice.roll_dice(10))