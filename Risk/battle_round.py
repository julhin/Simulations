import dice_rolls

class BattleRound:
    def __init__(self,attacker, defender):
        self.attackerArmies = attacker
        self.defenderArmies = defender 
    
    def fight(self, to_the_end = True):
        dice = dice_rolls.Dice()
        #winner = ""
        winnerSide = ""
        armiesLeft = 0
        while(self.attackerArmies > 0 and self.defenderArmies > 0):
            # fight a round 
            atk_dice = dice.roll_dice(self.getDice(self.attackerArmies), True)
            def_dice = dice.roll_dice(self.getDice(self.defenderArmies), True)

            #print(atk_dice, def_dice)
            atk_casualties, def_casualities = 0, 0
            for idx in range(0, min(len(def_dice),len(atk_dice))):
                if (atk_dice[idx] > def_dice[idx]):
                    def_casualities += 1
                else: 
                    atk_casualties += 1
            self.attackerArmies -= atk_casualties
            self.defenderArmies -= def_casualities
           
            #print(f"atk army loss: {atk_casualties} def army loss: {def_casualities}")
            if (self.attackerArmies <= 0):
                #winner = f"Defender won with {self.defenderArmies} left"
                armiesLeft = self.defenderArmies
                winnerSide = "def"
            if (self.defenderArmies <= 0):
                #winner= f"Attacker won with {self.attackerArmies} left"   
                armiesLeft = self.attackerArmies
                winnerSide = "atk"
        # DB Access: Winner und verbleibende Armeen
        #print(f"{winnerSide} : {armiesLeft}")
        return (winnerSide, armiesLeft)


    def getDice(self,armies):
        return min(3,armies)

if __name__ == "__main__":
    battle = BattleRound(10,10)
    battle.fight()