class ResultContainer:

    def __init__(self, battle_id, atk_start_armies, def_start_armies, winner, armies_left):
        self.battle_id = battle_id
        self.atk_start_armies = atk_start_armies
        self.def_start_armies = def_start_armies
        self.winner = winner
        self.armies_left = armies_left
    

    def __str__(self):
        """
        Return a string representation of the ResultContainer object.
        """
        return (f"Battle ID: {self.battle_id}\n"
                f"Attacking Armies Start: {self.atk_start_armies}\n"
                f"Defending Armies Start: {self.def_start_armies}\n"
                f"Winner: {self.winner}\n"
                f"Armies Left: {self.armies_left}")
                
    def send_to_DB(self):
        # draw counts as win for defender, because defender does not lose territory
        # check if all fields are filled 
        # then open DB Connection
        pass

if __name__ == "__main__":
    battle_result = ResultContainer(
    battle_id=1,
    atk_start_armies=100,
    def_start_armies=80,
    winner='atk',
    armies_left=20
    )
    print(battle_result)