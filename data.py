import requests
import pandas as pd
import numpy as np
from time import sleep
from dataclasses import dataclass

# Class to hold fighter specs
@dataclass
class Fighter:
    fighter_id: int
    name: str
    attackpoints: float # Carbs
    healthpoints: int # Energy kcal
    mass: int # Fats
    defencepoints: float # Proteins
    attack_time: float = 0
    alive: bool = True
    next_attack: float = 0

    # Method to calculate how frequently fighter attacks
    def time_to_attack(self) -> None:
        self.attack_time = self.attackpoints + self.defencepoints + self.mass

    #Method to calculate when next attack is going to happen
    def next_attack_time(self) -> None:
        self.next_attack += self.attack_time
        self.next_attack = round(self.next_attack,2)

# Get data
def fetch_data(food_list:list, header_data:dict)-> pd.DataFrame:
    df = pd.DataFrame()
    for food in food_list:
        response = requests.get(f'https://fineli.fi/fineli/api/v1/foods/?q={food}',headers=header_data).text
        temp = pd.read_json(response)
        df = pd.concat([df,temp])
        sleep(2)

    # Drop unnecessary columns
    df = df.drop(columns=['functionClass','ingredientClass','specialDiets','units','id','ediblePortion',
                        'themes','alcohol','organicAcids','sugarAlcohol','sugar','fiber','saturatedFat',
                        'energy','salt'])

    # Slice name
    df = pd.concat([df, df['name'].apply(pd.Series)], axis=1)
    df['nimi'] = df['fi']
    df = df.drop(columns=['name','sv','en','la','fi'])

    # Get type code
    df = pd.concat([df, df['type'].apply(pd.Series)], axis=1)
    df['type_code'] = df['code']
    df = df.drop(columns=['description','abbreviation','type','code'])

    # Slice preparationMethod code
    df = pd.concat([df, df['preparationMethod'].apply(pd.Series)], axis=1)
    df['prep'] = df[0]
    df = pd.concat([df, df['prep'].apply(pd.Series)], axis=1)
    df['prep_code'] = df['code']
    df = df.drop(columns=['preparationMethod',0,'prep','description', 'abbreviation','code'])

    # Drop prepared foods
    df = df[df['type_code'] != "DISH"]
    df = df[df['prep_code'] == "RAW"]
    df = df.assign(Index=range(len(df))).set_index('Index')

    df[['0','1','2','3']] = df['nimi'].str.split(',', expand=True)
    df['food'] = df['0']
    df = df.drop(columns=['nimi','0','1','2','3'])

    df = df.drop(columns=['type_code', 'prep_code'])
    table = pd.pivot_table(df,  values=['energyKcal','fat','protein','carbohydrate'],
                                index=['food'], 
                                aggfunc={   'energyKcal': np.mean,
                                            'fat': np.mean,
                                            'protein': np.mean,
                                            'carbohydrate': np.mean})
    table.reset_index(inplace=True)
    
    # Rounding values
    cols = ['energyKcal', 'fat', 'protein', 'carbohydrate']
    for c in cols:
        table[c] = table[c].round(decimals=2)
    
    return table

# Function to calculate happening of first attack for every fighter
def calculate_attack_times(*fighters:Fighter) -> None:
    for fighter in fighters:
        fighter.next_attack_time()

#Function to do initial setup of Fighters
def setup(data:list, fighter_num1:int, fighter_num2:int) -> Fighter:
    f1 = Fighter(1, data[fighter_num1][0],data[fighter_num1][1],data[fighter_num1][2],data[fighter_num1][3],data[fighter_num1][4])
    f1.time_to_attack()
    f2 = Fighter(2,data[fighter_num2][0],data[fighter_num2][1],data[fighter_num2][2],data[fighter_num2][3],data[fighter_num2][4])
    f2.time_to_attack()     
    calculate_attack_times(f1,f2)
    return f1,f2

