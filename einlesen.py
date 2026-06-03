from klassen import Angriffe, Pokemon
import csv

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
                atk_ls.append(Angriffe(name, int(atk)))
        return atk_ls
    except FileNotFoundError:
        print(f"{url} not found")

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
                Def = int(zeile[3].strip())
                typ = zeile[4].strip()
                pkm_ls.append(Pokemon(name, hp, atk, Def, typ, None))
        return pkm_ls
    except FileNotFoundError:
        print(f"{url} not found")