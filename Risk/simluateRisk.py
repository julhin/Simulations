import battle_round as br
import pandas as pd 
import result_container

def simulateRisk():
    # Wie Daten darstellen? 

    # wie viel Runs pro Runde 
    runs = 1000000
    runs = 3
    max_armies = 30
    max_armies = 5
    result = {}
    # verschachtelte Schleife und Tupel - Spaß :)
    result = []
    current_battle_id = 0
    # start at 1, because 0 is not valid attack
    for attackerArmies in range(1, max_armies):
        for defenderArmies in range(1,max_armies):
            attackerList = []
            defenderList = []
            for _ in range(0, runs):
                battle = br.BattleRound(attackerArmies, defenderArmies)
                battleResult = battle.fight()
                """ if (battleResult[0] == 'def'):
                    defenderList.append(battleResult[1])
                if(battleResult[0] == 'atk'):
                    attackerList.append(battleResult[1]) """
                #result[(attackerArmies, defenderArmies)][battleResult[0]].append(battleResult[1])
                battle_result_container = result_container.ResultContainer(
                    battle_id = current_battle_id,
                    atk_start_armies=attackerArmies,
                    def_start_armies=defenderArmies,
                    winner=battleResult[0],
                    armies_left=battleResult[1]
                )
                result.append(battle_result_container)
            current_battle_id += 1  
    for current_result in result:
        print(current_result)
    

if __name__ == "__main__":
    simulateRisk()