from dataclasses import dataclass

@dataclass
class Fighter:
    fighter_id: int
    name: str
    healthpoints: int
    attackpoints: float
    defencepoints: float
    mass: int
    attack_time: float = 0
    alive: bool = True
    next_attack: float = 0

    def time_to_attack(self) -> None:
        self.attack_time = self.attackpoints + self.defencepoints + self.mass

    def next_attack_time(self) -> None:
        self.next_attack += self.attack_time
        self.next_attack = round(self.next_attack,2)

class Turn:
    def calculate_damage(attacker_power:float, defender_strength:float) -> float:
        return round(attacker_power - defender_strength,2)

    def attack(attack_power:float, attacker:Fighter, defender:Fighter, attack_time:float) -> str:
        defender.healthpoints -= attack_power
        if defender.healthpoints <= 0:
            defender.healthpoints = 0
            defender.alive = False
            return f'{attack_time}s: {attacker.name} has done {attack_power} points of damage and won the battle!'
        else:
            return f'{attack_time}s: {attacker.name} has done {attack_power} points of damage! {defender.name} has {round(defender.healthpoints,2)} healthpoints left!'


