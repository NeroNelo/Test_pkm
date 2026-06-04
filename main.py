# GUI Neu machen
import copy
import time
import random
from klassen import Pokemon
from einlesen import atk_einlesen, pkm_einlesen
from pkm_generieren import get_pkm, get_attacken

GRUEN = "\033[32m"
ROT = "\033[31m"
GELB = "\033[33m"
LILA = "\033[35m"
RESET = "\033[0m"

atk_Feuer = atk_einlesen("ATK/atk_Feuer.csv")
atk_Wasser = atk_einlesen("ATK/atk_Wasser.csv")
atk_Pflanze = atk_einlesen("ATK/atk_Pflanze.csv")
atk_Elektro = atk_einlesen("ATK/atk_Elektro.csv")
atk_Normal = atk_einlesen("ATK/atk_Normal.csv")
attacken = [atk_Feuer, atk_Wasser, atk_Pflanze, atk_Elektro, atk_Normal]
pkm = pkm_einlesen("pokemon.csv")


def pkm_Fight(spieler_pkm: Pokemon, gegner_pkm: Pokemon):
    print(f"\n{GRUEN}Du startest mit {spieler_pkm.name}!{RESET}")
    print(f"{ROT}Ein feindliches {gegner_pkm.name} erscheinen!\nFight!!!{RESET}")
    time.sleep(1)
    while True:
        for i, att in enumerate(spieler_pkm.attacke):
            print(f"{GELB}{i + 1}. {att.name} ({att.atk} atk){RESET}")
        atk = int(input())
        x = gegner_pkm.take_dmg(spieler_pkm.atk, spieler_pkm.attacke[atk - 1].atk)
        print(f"{ROT}{gegner_pkm.name} hat {x} Schaden erlitten{RESET}")
        time.sleep(1)
        if gegner_pkm.hp <= 0:
            print(f"{LILA}{gegner_pkm.name} wurde besiegt!\nDu hast Gewonnen\nGlückwunsch!{RESET}")
            break
        else:
            print(f"{ROT}{gegner_pkm.name} hat noch {gegner_pkm.hp} HP{RESET}")
        time.sleep(1)
        print(f"{ROT}{gegner_pkm.name} greift an!{RESET}")
        rnd = random.randint(0, 3)
        print(f"{ROT}{gegner_pkm.name} setzt {gegner_pkm.attacke[rnd].name} ein!{RESET}")
        time.sleep(1)
        x = spieler_pkm.take_dmg(gegner_pkm.atk, gegner_pkm.attacke[atk - 1].atk)
        print(f"{GRUEN}Dein {spieler_pkm.name} hat {x} schaden erlitten{RESET}")
        time.sleep(1)
        if spieler_pkm.hp <= 0:
            print(f"{LILA}{spieler_pkm.name} wurden besiegt!\nDu hast leider verlohren!{RESET}")
            break
        else:
            print(f"{GRUEN}Dein {spieler_pkm.name} hat noch {spieler_pkm.hp} HP{RESET}")
        time.sleep(1)


def main():
    pkm1 = copy.copy(get_pkm(pkm))
    pkm2 = copy.copy(get_pkm(pkm))
    pkm1.attacke = get_attacken(attacken, pkm1.typ)
    pkm2.attacke = get_attacken(attacken, pkm2.typ)

    pkm_Fight(pkm1, pkm2)
    print("Spiel Zuende")


if __name__ == '__main__':
    main()
