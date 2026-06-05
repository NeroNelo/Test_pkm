# GUI Neu machen
import copy
import time
import random
from klassen import Pokemon,Attack
from einlesen import atk_einlesen, pkm_einlesen
from pkm_generieren import get_pkm, get_attacken, random_atk_levelup
from user_imput_handling import user_imput_1_to, user_imput_n0_y1

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
        atk = user_imput_1_to(4)
        x = gegner_pkm.take_dmg(spieler_pkm.atk, spieler_pkm.attacke[atk - 1].atk)
        print(f"{ROT}{gegner_pkm.name} hat {x} Schaden erlitten{RESET}")
        time.sleep(1)
        if gegner_pkm.hp <= 0:
            print(f"{LILA}{gegner_pkm.name} wurde besiegt!\nDu hast Gewonnen\nGlückwunsch!{RESET}")
            spieler_pkm.level_up()
            time.sleep(1)
            print(f"{GRUEN}Du hast ein Level Up Bekommen!{RESET}")
            time.sleep(1)
            new_attacke = random_atk_levelup(spieler_pkm, attacken)
            if  type(new_attacke) == Attack:
                print(f"\n\n{LILA}{spieler_pkm.name} kann {new_attacke.name} ({new_attacke.atk} atk) erlernen!\nMöchtest du sie erlernen ja/nein!{RESET}")
                if user_imput_n0_y1() == 1:
                    for i, att in enumerate(spieler_pkm.attacke):
                        print(f"{GELB}{i + 1}. {att.name} ({att.atk} atk){RESET}")
                    print(f"{LILA}Welche Attacke möchstest du ersetzen?{RESET}")
                    x =user_imput_1_to(4)
                    if spieler_pkm.attacke_ersetzen(x-1,new_attacke) == 1:
                        print(f"{GRUEN}Neue Attacke erlernt!{RESET}")
                    pass

            print(f"{GRUEN}Dein Pokemon wurde geheilt!{RESET}")
            time.sleep(1)
            break
        else:
            print(f"{ROT}{gegner_pkm.name} hat noch {gegner_pkm.hp} HP{RESET}")
        time.sleep(1)
        print(f"{ROT}{gegner_pkm.name} greift an!{RESET}")
        rnd = random.randint(0, 3)
        print(f"{ROT}{gegner_pkm.name} setzt {gegner_pkm.attacke[rnd].name} ein!{RESET}")
        time.sleep(1)
        x = spieler_pkm.take_dmg(gegner_pkm.atk, gegner_pkm.attacke[rnd].atk)
        print(f"{GRUEN}Dein {spieler_pkm.name} hat {x} schaden erlitten{RESET}")
        time.sleep(1)
        if spieler_pkm.hp <= 0:
            print(f"{LILA}{spieler_pkm.name} wurden besiegt!\nDu hast leider verlohren!{RESET}")
            break
        else:
            print(f"{GRUEN}Dein {spieler_pkm.name} hat noch {spieler_pkm.hp} HP{RESET}")
        time.sleep(1)


def main():

    spieler_level = 5
    pkm1 = get_pkm(pkm, level=spieler_level)
    pkm1.attacke = get_attacken(attacken, pkm1.typ)


    while pkm1.hp >= 0:
        gegner_level = max(1, pkm1.level + random.randint(-5, 5))
        pkm2 = get_pkm(pkm, level=gegner_level)
        pkm2.attacke = get_attacken(attacken, pkm2.typ)

        print(f"\n{LILA}Dein {pkm1.name} (Lv. {pkm1.level}, {pkm1.hp} HP) VS {ROT}{pkm2.name} (Lv. {pkm2.level}, {pkm2.hp} HP)!{RESET}")

        pkm_Fight(pkm1, pkm2)
    print("Spiel Zuende")


if __name__ == '__main__':
    main()
