import abc

from name_service import NameService


class Pokemon(NameService, metaclass=abc.ABCMeta):
    def __init__(self, name, type1, type2, hp):
        self.__name = name  # __で名前修飾する
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abc.abstractmethod
    def attack(self):
        pass

    def changeName(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self.__name = new_name

    def getName(self):
        return self.__name


class Pikachu(Pokemon):
    def attack(self):
        print(f"{self.getName()} の10万ボルト!")


class Zenigame(Pokemon):
    def attack(self):
        print(f"{self.getName()} のみずでっぽう!")
