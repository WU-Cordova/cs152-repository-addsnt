import random
from character import Character

class Game:
    def __init__(self, player1: Character, player2: Character):
        self._player1 = player1
        self._player2 = player2

    def attack(self, attacker: Character, defender: Character):
        roll_dice = random.randint(1,6)
        damage_delt = roll_dice*attacker.attack_power
        defender.health -= damage_delt
        # print("Attacker has rolled "+roll_dice+". Damage dealt: "+damage_delt)
        # print("Defender health: "+ defender.health)


    def start_battle(self):
        attacker, defender = self._player1, self._player2
        # print("Game has started " + self._player1 + " is the attacker, "+self._player2+" is the defender")
        while attacker.health > 0 and defender.health > 0:
            self.attack(attacker, defender)
            if defender.health <= 0:
                # print("Game over, defender has been defeated.")
                break
            attacker, defender = defender, attacker