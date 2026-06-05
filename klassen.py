import random


class Pokemon:
    def __init__(self, name: str, base_hp: int, base_atk: int, base_defence: int, typ: str, level: int = 1,
                 attacke: list = None):
        self.__name = name
        self.__level = level
        self.__typ = typ
        self.__attacke = attacke

        # Basis-Werte aus der pokemon.csv
        self.__base_hp = base_hp
        self.__base_atk = base_atk
        self.__base_defence = base_defence

        # Stats werden basierend auf dem Level berechnet
        self.recalculate_stats()

    def recalculate_stats(self):
        # HP steigt spürbar pro Level, ATK und DEF linear.
        self.__hp = int(self.__base_hp + (self.__base_hp * 0.05 * self.__level))
        self.__max_hp = self.__hp
        self.__atk = int(self.__base_atk + (self.__base_atk * 0.02 * self.__level))
        self.__defence = int(self.__base_defence + (self.__base_defence * 0.02 * self.__level))

    @property
    def level(self):
        return self.__level

    # Falls ein Pokémon ein Level-Up macht
    def level_up(self):
        self.__level += 1
        self.recalculate_stats()

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value: int):
        self.__hp = value

    def take_dmg(self, atk_pkm: int, atk_attacke: int):
        # Deine Schadensformel bleibt gleich, nutzt jetzt aber die skalierten Werte
        dmg = (atk_pkm / max(1, self.defence)) * atk_attacke * 0.5
        dmg = max(1, int(dmg * random.uniform(0.85, 1.00)))
        self.__hp -= dmg
        return dmg

    @property
    def atk(self):
        return self.__atk

    @property
    def defence(self):
        return self.__defence

    @property
    def typ(self):
        return self.__typ

    @property
    def attacke(self):
        return self.__attacke

    @attacke.setter
    def attacke(self, angriffe: list):
        self.__attacke = angriffe
    def attacke_ersetzen(self,index:int, neue_attacke: Attack):
        self.__attacke[index] = neue_attacke
        return 1



class Attack:
    def __init__(self, name: str, atk: int):
        self.name = name
        self.atk = atk
