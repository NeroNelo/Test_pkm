from klassen import Attack, Pokemon
import csv

# Atk einlesen aus CSV Datei
def atk_einlesen(url):
    atk_ls = []
    try:
        with open(url, "r", encoding="utf-8") as datei:
            csv_zeile = csv.reader(datei, delimiter=",")
            for zeile in csv_zeile:
                if not zeile:
                    continue
                name = zeile[0].strip()
                atk = zeile[1].strip()
                atk_ls.append(Attack(name, int(atk)))
        return atk_ls
    except FileNotFoundError:
        print(f"{url} not found")

# Alle PKM aus CSV Datei einlesen
def pkm_einlesen(url):
    pkm_ls = []
    try:
        with open(url, "r", encoding="utf-8") as datei:
            csv_zeile = csv.reader(datei, delimiter=",")
            for zeile in csv_zeile:
                if not zeile:
                    continue
                name = zeile[0].strip()
                hp =  int(zeile[1].strip())
                atk = int(zeile[2].strip())
                defence = int(zeile[3].strip())
                typ = zeile[4].strip()
                pkm_ls.append(Pokemon(name, hp, atk, defence, typ, 1,None))
        return pkm_ls
    except FileNotFoundError:
        print(f"{url} not found")