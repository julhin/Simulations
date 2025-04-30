import random
import json

max_atk_dice = 3
max_def_dice = 3
iterations = 100


def dice_roll(sides=6):
    return random.randint(1, sides)


def checkDiceAtttacker(armies: int):
    if armies >= max_atk_dice:
        return max_atk_dice
    return armies


def checkDiceDefender(armies: int):
    if armies >= max_def_dice:
        return max_def_dice
    return armies


def battleDiceRoll(dice: int):
    tmp = []
    for i in range(0, dice):
        tmp.append(dice_roll())
    return tmp


def battleRound(atkDice: int, defDice: int):
    attacker = battleDiceRoll(atkDice)
    defender = battleDiceRoll(defDice)
    attacker.sort(reverse=True)
    defender.sort(reverse=True)
    # compare resulst and return casualaties

    # print(attacker)
    # print(defender)
    # print("----------")
    casAtk = 0
    casDef = 0

    if (len(defender) <= len(attacker)):
        dicetocheck = len(defender)
    else:
        dicetocheck = len(attacker)

    for i in range(0, dicetocheck):
        if (defender[i] >= attacker[i]):
            casAtk = casAtk + 1
        else:
            casDef = casDef + 1
    return (casAtk, casDef)


def battle(attacker: int, defender: int):
    # fight sequence
    casulatiesATK = 0
    casulatiesDEF = 0
    while True:
        # print(f"Armies attacker: {attacker}")
        # print(f"Armies defender: {defender}")
        # return value of winner: attacker == 0 return defneder victory
        if (attacker == 0):
            # def wins
            return 0, casulatiesATK, casulatiesDEF
        if (defender == 0):
            # atk wins
            return 1, casulatiesATK, casulatiesDEF

        atkDice = checkDiceAtttacker(attacker)
        defDice = checkDiceDefender(defender)
        result = battleRound(atkDice, defDice)
        attacker = attacker - result[0]
        defender = defender - result[1]
        casulatiesATK += result[0]
        casulatiesDEF += result[1]


def getUserInputInteger(txt):
    cnt = 0
    while cnt < 10:
        s = input(txt)
        try:
            x = int(s)
            return x
        except:
            print("please enter a valid input")
            cnt += 1
            continue


if __name__ == "__main__":
    # make fiel for std input
    if getUserInputInteger("standard values? (1 yes, 0 no): ") == 1:
        # read standard values
        pass
    else:
        def_dice = getUserInputInteger("Enter defender dice (2,3): ")
        iterations = getUserInputInteger("Enter iterations: ")
        runs = getUserInputInteger("Enter runs: ")
        armeisAtk = getUserInputInteger("Enter attacker armies: ")
        armeisDEF = getUserInputInteger("Enter defender armies: ")
        max_def_dice = def_dice

    # battleResults = []
    casulatiesATK = 0
    casulatiesDEF = 0
# dict structure: number of battles
    results = dict()
    results["winner"] = []
    results["casATK"] = []
    results["casDEF"] = [3]
    for _ in range(runs):
        for i in range(iterations):
            resultBattle, casulatiesATK, casulatiesDEF = battle(
                armeisAtk, armeisDEF)
            # battleResults.append(resultBattle)
            results["winner"].append(resultBattle)
            results["casATK"].append(casulatiesATK)
            results["casDEF"].append(casulatiesDEF)

    print(results)
    winsAtk, winsDef = 0, 0
    for winner in results.items():
        print(winner)
        if (winner == 1):
            winsAtk += 1
        else:
            winsDef += 1
    print("attacker wins: " + str(winsAtk))
    print("defender wins: " + str(winsDef))
