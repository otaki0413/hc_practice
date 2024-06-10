import abc

from name_service import NameService


class Player(NameService, metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.__name = name  # 名前修飾する

    def changeName(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self.__name = new_name

    def getName(self):
        return self.__name
