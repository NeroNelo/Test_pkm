class Pokemon:
    def __init__(self, name: str,hp: int,atk:int, Def: int,typ: str, attacke: list[Angriffe]|None ):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__Def = Def
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

    @property
    def atk(self):
        return self.__atk

    @property
    def Def(self):
        return self.__Def

    @property
    def typ(self):
        return self.__typ

    @property
    def attacke(self):
        return self.__attacke
    @attacke.setter
    def attacke(self, angriffe: list[Angriffe]):
        self.__attacke = angriffe



class Angriffe:
    def __init__(self, name: str, atk: int):
        self.name = name
        self.atk = atk