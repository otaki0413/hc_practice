import abc


class NameService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def changeName(self, new_name):
        pass

    @abc.abstractmethod
    def getName(self):
        pass


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


class Player(NameService, metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.__name = name

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


def main():
    pika = Pikachu("ピカチュウ", "でんき", "", 100)
    pika.attack()
    pika.changeName("テキセツ")
    print(pika.getName())
    pika.changeName("うんこ")
    print(pika.getName())

    kei = Player("けい")
    kei.changeName("けい2")
    print(kei.getName())
    kei.changeName("うんこ")
    print(kei.getName())


if __name__ == "__main__":
    main()
