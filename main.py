from fight import Turn
from time import sleep
from data import Fighter, setup, FOODS
import random

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

def determine_fighters() -> Fighter:
    # Pick random fghters
    index1 = random.randint(0,len(FOODS))
    index2 = random.randint(0,len(FOODS))
    if index1 == index2:
        index2 = random.randint(0,len(FOODS))
    else:
        fighters_pool = setup(index1,index2)
    
    return fighters_pool

def main() -> None:
    fighters_pool = determine_fighters()
    while True:
        # Determine who is going to attack next and when
        next_attack_to_happen = attack_turn(fighters_pool[0],fighters_pool[1])
        attacker = next_attack_to_happen[0]
        time_of_attack = next_attack_to_happen[1]

        #Assign defending role
        if attacker.fighter_id == fighters_pool[0].fighter_id:
            defender = fighters_pool[1]
        else:
            defender = fighters_pool[0]

        #ATTACK!
        print(do_turn(attacker, defender,time_of_attack))
        
        #Count next time of attack for attacker
        attacker.next_attack_time()
        
        #Check if defender got knocked out
        if defender.alive is False:
            break   
        
        sleep(1)

main()