import time
import random
from klassen import Pokemon, Angriffe
from einlesen import atk_einlesen, pkm_einlesen
from pkm_generieren import get_pkm, get_attacken

atk_Feuer = atk_einlesen("ATK/atk_Feuer.csv")
atk_Wasser = atk_einlesen("ATK/atk_Wasser.csv")
atk_Pflanze = atk_einlesen("ATK/atk_Pflanze.csv")
atk_Elektro = atk_einlesen("ATK/atk_Elektro.csv")
atk_Normal = atk_einlesen("ATK/atk_Normal.csv")
attacken= [atk_Feuer,atk_Wasser,atk_Pflanze,atk_Elektro, atk_Normal]
print(attacken[0][0].name)
pkm = pkm_einlesen("pokemon.csv")

def gameState(spieler_pkm: Pokemon, gegner_pkm: Pokemon ):
    print(f"Ein feindliches {gegner_pkm.name} erscheinen!\nFight!!!")
    time.sleep(1)
    while True:
        print(f"1. {spieler_pkm.attacke[0].name} ({spieler_pkm.attacke[0].atk} atk)\n2. {spieler_pkm.attacke[1].name} ({spieler_pkm.attacke[1].atk} atk)\n3. {spieler_pkm.attacke[2].name} ({spieler_pkm.attacke[2].atk} atk)\n4. {spieler_pkm.attacke[3].name} ({spieler_pkm.attacke[3].atk} atk)")
        atk = int(input())
        gegner_pkm.hp = spieler_pkm.attacke[atk-1].atk
        print(f"{gegner_pkm.name} hat {spieler_pkm.attacke[atk - 1].atk} Schaden erlitten")
        time.sleep(1)
        if gegner_pkm.hp <=0:
            print(f"{gegner_pkm.name} wurde besiegt")
            break
        else:
            print(f"{gegner_pkm.name} hat noch {gegner_pkm.hp} HP")
        time.sleep(1)
        print(f"{gegner_pkm.name} greift an!")
        rnd = random.randint(0, 3)
        print(f"{gegner_pkm.name} setzt {gegner_pkm.attacke[rnd].name} ein!")
        time.sleep(1)
        spieler_pkm.hp=gegner_pkm.attacke[rnd].atk
        print(f"{spieler_pkm.name} hat {gegner_pkm.attacke[rnd].atk} schaden erlitten")
        time.sleep(1)
        if spieler_pkm.hp <= 0:
            print(f"{spieler_pkm.name} wurden besiegt")
            break
        else:
            print(f"{spieler_pkm.name} hat noch {spieler_pkm.hp} HP")
        time.sleep(1)


def main():

    pkm1= get_pkm(pkm)
    pkm2= get_pkm(pkm)

    pkm1.attacke = get_attacken(attacken,pkm1.typ)
    pkm2.attacke = get_attacken(attacken,pkm2.typ)

    gameState(pkm1, pkm2)
    print("Spiel Zuende")

if __name__ == '__main__':
    main()
