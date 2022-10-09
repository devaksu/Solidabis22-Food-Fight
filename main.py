from fight import Fighter, Turn
from time import sleep

#TODO: Determine which player's turn to attack

def calculate_attack_times(*fighters:Fighter):
    for fighter in fighters:
        fighter.next_attack_time()
    
def do_turn(attacker:Fighter, defender:Fighter, attack_time:float):
    dmg = Turn.calculate_damage(attacker.attackpoints, defender.defencepoints)
    attk = Turn.attack(dmg, attacker, defender, attack_time)
    return attk

def attack_turn(*fighters: Fighter):
    next_attacker = [None, None]
    for fighter in fighters:
        if next_attacker[1] is None or fighter.next_attack < next_attacker[1]:
            next_attacker = fighter, fighter.next_attack
    return next_attacker 

def main():
    f1 = Fighter(1,"Carrot", 33, 5.6, 0.6, 0.2)
    f1.time_to_attack()
    f2 = Fighter(2,"Broccoli", 35, 7.6, 0.4, 0.7)
    f2.time_to_attack()     
    calculate_attack_times(f1,f2)
    while True:

        next_attack_to_happen = attack_turn(f1,f2)
        attacker = next_attack_to_happen[0]
        time_of_attack = next_attack_to_happen[1]
        if attacker.fighter_id == 1:
            defender = f2
        else:
            defender = f1

        print(do_turn(attacker, defender,time_of_attack))
        attacker.next_attack_time()
        if defender.alive is False:
            break   
        sleep(1)

main()