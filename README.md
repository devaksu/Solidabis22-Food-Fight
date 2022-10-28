# It's a **Food Fight**!
https://koodihaaste.solidabis.com/intro

Ruokarähinä: Porkkana ja paprika tappeli, kumpi otti turpaan?

"Tiiätkö transformerssit? No nää ei oo niitä, mutta ne vetää toisiaan pataan silti. Vähän niinkuin ultimate fighter, mutta tyyppien sijaan siellä on ruokaa".
Ruokarähinässä kaksi tai useampaa erilaista ruokaa käy vastakkain todistaakseen kuka on vahvin! Tässä jännittävässä taistelussa pääsemme näkemään joitain maailman vahvimpia ruokia ja selvittämään mikä tekee niistä niin erikoisia. Maukkaimmista ja herkullisimmista vahvimpiin ja tehokkaimpiin, katsotaan, mikä ruoka hallitsee yli kaikkien!

Usein ajattelemme että vahvin tai paras ruoka on se, josta saamme eniten ravinteita. Mutta ei tänään! Tässä taistelussa voimakkaimpina ovat mättöruoat. Suurimmat määrät kaloreita ja hiilareita tuovat voiton kotiin. Go karkkipäivä!!! Vai tuovatko sittenkään? Otetaan selvää...

## Tehtävä

Tehtävänäsi on toteuttaa ruokarähinä teemainen taistelu, jossa ruoat taistelevat keskenään erilaisilla statseilla.
Tehtävän toteutusta varten sinun tulee hakea eri ruokien ravintosisällöt ja toteuttaa näistä statsit, joiden perusteella ruoat taistelevat keskenään.
Toteutuksessa käytettävät teknologiat ovat vapaasti päätettävissäsi, ja voit toteuttaa tehtävän frontend-, backend- tai fullstack-toteutuksena (kts. palkintoluokat)

### Sovelluksessa tulee olla seuraavat toiminnot:

    - Eri ravintosisältöjen haku ulkoisesta lähteestä (esim. Fineli API tai jokin muu vastaava kuten CSV-tiedosto)
    - Ravintosisältöjen muuntaminen hahmoluokkiin
    - Logiikan toteutus kahden ruokahahmon väliseen kaksintaisteluun
    - Tulosten esitys tekstimuotoisena rajapinta vastauksena tai visuaalisesti Frontendilla

### Statsit:
Perus statsit täytyy löytyä ja olla kaavan mukaan. On kuitenkin lupa lisätä taisteluihin satunnaisuutta:

    - Energia (kcal) = Health Points eli kestopisteet.
    - Hiilihydraatit (g) = Hyökkäysvoima
    - Proteiinit (g) = Puolustusvoima (voidaan käyttää esim. prosentuaalisesti, koska maksimi on tietty 100)
    - Rasvat ei erikseen lisää mitään statsia, mutta enemmän rasvaa = enemmän energiaa = enemmän helaa
    - Hiilihydraattien, rasvojen ja proteiinien yhteenlaskettu grammamäärä = Hitaus. (tai käänteisellä arvolla hyökkäysnopeus)

## Technical stuff:

### Specs:

    - Developed on MacOS Monterey and Windows 11.
    - Dockerized and tested on MacOS Ventura
    - Python 3.10.4.
    - FastAPI and uvicorn.
    - Firefox shows output very readably by default

### How to run:
0. (Install Docker)
1. Clone the repo
2. Make sure Docker is running and type to terminal command "docker compose up --build"
3. Wait for a sec while Docker is building the image and container
4. Open up a new Firefox tab and head for 0.0.0.0:8008/fighters to see all available characters
5. 0.0.0.0:8008 provides you a exiting fight between two random characters
6. (Refresh page for a new one)
7. Kill using Ctrl + C

## What is happening here?
### data.py:
    - first there is Fighter dataclass to hold information and with some assistive methods
    - fetch_data() connects to Fineli API and gets data for provided list of foods. 
    - After fetching data is being manipulated for proper use. Basically dropping columns, slicing data and dropping more columns
    - Some values may be mean of multiple different products (like apple)
    - calculate_attack_times() calculates next possible attacks for each fighter
    - setup() creates two different fighters for the match
    
### fight.py:
    - Class Turn holds events that happen on every turn
    - calculate_damage() reduces attacker's power depending on defender's defence power
    - attack() function makes attack and checks if defender still standing
    - attack_turn() checks whose turn is to attack next and when
    - determine_fighters() randomly chooses two fighters
    - start() creates battlelog and initialises it
    
### api.py:
    - first some constants
    - helper function write_result() to write events to log
    - fighters() function is FastAPI endpoint for fighters (I should add more data here and maybe fighter cards)
    - battle() function gathers everything up in this project
    - first we check if log exists and delete it if it does
    - determine who is going to attack next and when
    - assign defending role
    - do attack and update log
    - determine attackers next time of attack
    - if defender is knocked out, end fight
    - finally read lines of battlelog and provide them for endpoint
    
