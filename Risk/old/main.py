import dice_rolls as dice
import time as tm 
from functools import reduce
from operator import mul


def main():
    start = tm.time()
    tries = 1000
    # schlangen magic
    risk_dice = dice.Dice()
    # store results 
    result = 0
    for i in range (0, tries):
        roll = risk_dice.roll_dice(rolls=6)
        if 6 in roll:
            result += 1
    end = tm.time()

    #print(f"Chance of getting on six on 6 dice: {round((result / tries) * 100, 2)}%")
    #print(f"time elapsed: {round(end - start, 2)} secs")
    return round((result / tries) * 100, 2)

if __name__ == "__main__":
    runs = 10000
    result = 0
    start = tm.time()
    for i in range (0, runs):
        result += main()
    end = tm.time()
    print(f"{round((result / runs),2)}%")
    print(f"time elapsed: {round(end - start, 2)} secs")