from data import Fighter

class Turn:
    # Take Attackpoints and subtract defender's defencepoints to get the power of attack
    def calculate_damage(attacker_power:float, defender_strength:float) -> float:
        return round(attacker_power - defender_strength,2)

    #Method to make an attack
    def attack(attack_power:float, attacker:Fighter, defender:Fighter, attack_time:float) -> str:
        defender.healthpoints -= attack_power
        if defender.healthpoints <= 0:
            defender.healthpoints = 0
            defender.alive = False
            return f'{attack_time}s: {attacker.name} has done {attack_power} points of damage and won the battle! \n \nWINNER: {attacker.name}'
        else:
            return f'{attack_time}s: {attacker.name} has done {attack_power} points of damage! {defender.name} has {round(defender.healthpoints,2)} healthpoints left!'

