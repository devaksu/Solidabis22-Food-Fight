from data import Fighter, setup
import random

class Turn:
    # Take Attackpoints and subtract defender's defencepoints to get the power of attack
    def calculate_damage(attacker_power:float, defender_strength:float) -> float:
        return round(attacker_power * (1 - (defender_strength/100)),2)

    #Method to make an attack
    def attack(attack_power:float, attacker:Fighter, defender:Fighter, attack_time:float) -> str:
        defender.healthpoints -= attack_power
        if defender.healthpoints <= 0:
            defender.healthpoints = 0
            defender.alive = False
            return f'{attack_time:05.2f}s: {attacker.name} has done {attack_power} points of damage and knocked out {defender.name}! \n {87*"="}\nWINNER: {attacker.name} with {attacker.healthpoints:05.2f} healthpoints left!'
        else:
            return f'{attack_time:05.2f}s: {attacker.name} has done {attack_power} points of damage! {defender.name} has {defender.healthpoints:05.2f} healthpoints left!'


# Actions for every turn    
def do_turn(attacker:Fighter, defender:Fighter, attack_time:float):
    dmg = Turn.calculate_damage(attacker.attackpoints, defender.defencepoints)
    attk = Turn.attack(dmg, attacker, defender, attack_time)
    return attk

# Function to determine whose turn is to attack next
def attack_turn(*fighters: Fighter):
    next_attacker = [None, None]
    for fighter in fighters:
        if next_attacker[1] is None or fighter.next_attack < next_attacker[1]:
            next_attacker = [fighter, fighter.next_attack]
    return next_attacker 

# Pick two random fighters
def determine_fighters(data:list,foods:list) -> Fighter:
    index1 = random.randint(0,len(foods)-1)
    index2 = random.randint(0,len(foods)-1)
    if index1 == index2:
        index2 = random.randint(0,len(foods))
    else:
        fighters_pool = setup(data,index1,index2)
    
    return fighters_pool

def start(file:str) -> None:
    with open(file, 'a') as f:
        f.write(f"{30*'='} Welcome to the FOOD FIGHT!{30*'='}" + '\n')
        f.write(f'{87*"="}\n')

        f.write(f"LET'S GET READY TO RUMBLE!!" + '\n')
