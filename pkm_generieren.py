from klassen import Pokemon, Attack
import random

# Holt ein Random PKM aus der liste
def get_pkm(pkm_ls:list[Pokemon])->Pokemon:
    return pkm_ls[random.randint(0, len(pkm_ls) - 1)]

# Generiert die 4 Attacken für das Pokemon abhängig von seinem Typ
def get_attacken(attacken_ls:list,typ : str)->list[Attack]:
    ls = [Attack]
    if typ == 'Feuer':
        ls =attacken_ls[0]
    if typ == 'Wasser':
        ls =attacken_ls[1]
    if typ == 'Pflanze':
        ls =attacken_ls[2]
    if typ == 'Elektro':
        ls =attacken_ls[3]
    if typ == 'Normal':
        ls =attacken_ls[4]
    a = []
    for i in range(4):
        a.append(ls[random.randint(0, len(ls) - 1)])
    return a
