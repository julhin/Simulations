import battle_round as br
import pandas as pd 

def simulateRisk():
    # Wie Daten darstellen? 

    # wie viel Runs pro Runde 
    runs = 1000000
    runs = 1
    max_armies = 30
    result = {}
    # verschachtelte Schleife und Tupel - Spaß :)
    result = {}
    for attackerArmies in range(0, max_armies):
        for defenderArmies in range(0,max_armies):
            attackerList = []
            defenderList = []
            for _ in range(0, runs):
                battle = br.BattleRound(attackerArmies, defenderArmies)
                battleResult = battle.fight()
                if (battleResult[0] == 'def'):
                    defenderList.append(battleResult[1])
                if(battleResult[0] == 'atk'):
                    attackerList.append(battleResult[1])
                
                result[(attackerArmies, defenderArmies)][battleResult[0]].append(battleResult[1])
    print(result)

if __name__ == "__main__":
    simulateRisk()