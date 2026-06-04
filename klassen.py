import random


class Pokemon:
    def __init__(self, name: str,hp: int,atk:int, defence: int,typ: str, attacke: list[Attack]|None ):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__defence = defence
        self.__typ = typ
        self.__attacke = attacke
    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, damage: int):
        self.__hp -= damage

    def  take_dmg(self, atk_pkm: int, atk_attacke:int):
        dmg  = (atk_pkm/max(1,self.defence))*atk_attacke  *0.5
        dmg = max(1,int(dmg * random.uniform(0.85,1.00)))
        print(dmg)
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
    def attacke(self, angriffe: list[Attack]):
        self.__attacke = angriffe



class Attack:
    def __init__(self, name: str, atk: int):
        self.name = name
        self.atk = atk