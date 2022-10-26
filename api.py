from fastapi import FastAPI
from fight import do_turn, attack_turn, determine_fighters, start
from data import fetch_data
import os

FILE = 'battle.txt'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
FOODS = ['omena','appelsiini','porkkana', 'parsakaali', 'peruna', 'banaani', 'lanttu','tomaatti','avokado']
DATA = fetch_data(FOODS, HEADERS).values.tolist()

def write_result(data:str) -> None:
    with open(FILE, 'a') as f:
        f.write(data + '\n')

app = FastAPI()

@app.get("/")
def battle() -> list[str]:
    if os.path.exists(FILE):
        os.remove(FILE)

    fighters_pool = determine_fighters(DATA,FOODS)
    start(FILE)
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
        turn = do_turn(attacker, defender,time_of_attack)
        write_result(turn)
        
        #Count next time of attack for attacker
        attacker.next_attack_time()
        
        #Check if defender got knocked out
        if not defender.alive:
            break
    
    # Read saved data
    with open(FILE,'r') as f:
        output_list = f.readlines()          
    
    return output_list    