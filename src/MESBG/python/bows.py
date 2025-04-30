import random
import numpy as np
from array import *
import container

wound_chart = [
        ["4", "5", "5", "6", "6", "6/4", "6/5", "6/6", "-", "-"],
        ["4", "4", "5", "5", "6", "6", "6/4", "6/5", "6/6", "-"],
        ["3", "4", "4", "5", "5", "6", "6", "6/4", "6/5","6/6"],
        ["3", "3", "4", "4", "5", "5", "6", "6", "6/4","6/5"],
        ["3", "3", "3", "4", "4", "5", "5", "6", "6","6/4"],
        ["3", "3", "3", "3", "4", "4", "5", "5", "6","6"],
        ["3", "3", "3", "3", "3", "4", "4", "5", "5","6"],
        ["3", "3", "3", "3", "3", "3", "4", "4", "5","5"],
        ["3", "3", "3", "3", "3", "3", "3", "4", "4","5"],
        ["3", "3", "3", "3", "3", "3", "3", "3", "4","4"],
        ]

def dice_roll(sides = 6):
    return random.randint(1,sides)


def ranged_attack(attacker, defender):
    if (not isinstance(attacker, container.Unit)) :
        print("hello")
    if (not isinstance(defender, container.Unit)) :
        print("hello")


    strength = attacker.strength
    defense = defender.defense
    
    hit = perform_ranged_attack(strength, defense)

    

def perform_ranged_attack(atk_strength, def_defense):
    value = compare_characteristics(atk_strength, def_defense)
    if (value == -1):
        return False
    if (value.__contains__('/')):
        tmp = value.split('/')
        if (len(tmp) != 2):
            #raise error -> data is corrupt
            return false 
        roll = dice_roll()
        if (roll >= value[0]):
            return dice_roll() >= value[1]
    return dice_roll() >= int(value)




def compare_characteristics(strength, defense):
    value = wound_chart[strength][defense]
    if (value == '-'):
        return -1
    return value


def main():

 
    dale_archer = container.Unit(6, '4/3', 4, 5, 1, 1, 4)
    print("Dale Archer")
    print(dale_archer.toString())
    legolas = container.HeroUnit(6,'5/3', 4, 6, 2, 3, 5, 2, 2, 2)
    print("Legolas")
    print(legolas.toString())

    ranged_attack(legolas, dale_archer)
    # for i in range(10):

    #     if (ranged_attack(3, 6) == True):
    #         print("Hit")
    #     else:
    #         print("Miss")


if __name__ == "__main__":
    main()    
