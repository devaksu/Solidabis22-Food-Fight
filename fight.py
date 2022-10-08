from dataclasses import dataclass
from time import sleep
from xmlrpc.client import Boolean

@dataclass
class Fighter:
    name: str
    healthpoints: int
    attackpoints: float
    defencepoints: float
    mass: int
    alive: bool = True

    def time_to_attack(self) -> float:
        attack_time = self.attackpoints + self.defencepoints + self.mass
        return round(attack_time,1)


f1 = Fighter("Carrot", 33, 5.6, 0.6, 0.2)
f2 = Fighter("Broccoli", 35, 6.6, 0.4, 0.7)

class Turn:
    def calculate_damage(attacker_power:float, defender_strength:float) -> float:
        return round(attacker_power - defender_strength,2)

    def attack(attack_power:float, attacker:Fighter, defender:Fighter) -> str:
        defender.healthpoints -= attack_power
        if defender.healthpoints <= 0:
            defender.healthpoints = 0
            defender.alive = False
        else: 
            return f'{attacker.name} has done {attack_power} points of damage! {defender.name} has {round(defender.healthpoints,2)} healthpoints left!'

#TODO: Determine which player's turn to attack

def do_turn(attacker:Fighter, defender:Fighter):
    dmg = Turn.calculate_damage(attacker.attackpoints, defender.defencepoints)
    print(dmg)
    attk = Turn.attack(dmg, attacker, defender)
    print(attk)
    sleep(1)

attacker = f1
defender = f2

while attacker.alive and defender.alive:
    attacker = f1
    defender = f2
    do_turn(attacker, defender)

