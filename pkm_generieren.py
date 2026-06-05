from klassen import Pokemon, Attack
import random
import copy
from user_imput_handling import user_imput_1_to

# Holt ein Random PKM aus der liste
def get_pkm(pkm_ls: list[Pokemon], level: int = 5) -> Pokemon:

    basis_pkm = pkm_ls[random.randint(0, len(pkm_ls) - 1)]
    neues_pkm = copy.copy(basis_pkm)
    # Level und Stats neu berechnen
    neues_pkm._Pokemon__level = level
    neues_pkm.recalculate_stats()

    return neues_pkm

# Generiert die 4 Attacken für das Pokemon abhängig von seinem Typ
def get_attacken(attacken_ls:list[Attack],typ : str)->list[Attack]:
    ls = [Attack]
    match typ:
        case "Feuer":
            ls =attacken_ls[0]
        case"Wasser":
            ls =attacken_ls[1]
        case"Pflanze":
            ls =attacken_ls[2]
        case"Elektro":
            ls =attacken_ls[3]
        case"Normal":
            ls =attacken_ls[4]
    a = []
    for i in range(4):
        a.append(ls[random.randint(0, len(ls) - 1)])
    return a

def random_atk_levelup(pkm:Pokemon,attacken_ls:list[Attack]):
    if pkm.level%5==0:
        ls = []
        match pkm.typ:
            case "Feuer":
                ls = attacken_ls[0]
            case "Wasser":
                ls = attacken_ls[1]
            case "Pflanze":
                ls = attacken_ls[2]
            case "Elektro":
                ls = attacken_ls[3]
            case "Normal":
                ls = attacken_ls[4]
        while True:
            attacke = ls[random.randint(0, len(ls) - 1)]
            if attacke not in pkm.attacke:

                return attacke
    else:
        return 0


