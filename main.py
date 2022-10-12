from fight import Fighter, Turn
from time import sleep

# Function to calculate happening of first attack for evert fighter
def calculate_attack_times(*fighters:Fighter):
    for fighter in fighters:
        fighter.next_attack_time()

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

#Function to do initial setup of Fighters
def setup() -> Fighter:
    f1 = Fighter(1,"Carrot", 53, 15.6, 0.6, 0.2)
    f1.time_to_attack()
    f2 = Fighter(2,"Broccoli", 35, 7.6, 0.4, 0.7)
    f2.time_to_attack()     
    calculate_attack_times(f1,f2)
    return f1,f2

def main():
    fighters_pool = setup()
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