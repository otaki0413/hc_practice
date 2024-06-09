import abc


class Pokemon(metaclass=abc.ABCMeta):
    def __init__(self, name, type1, type2, hp):
        self.__name = name  # __で名前修飾する
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abc.abstractmethod
    def attack(self):
        pass

    def changeName(self, new_name):
        # 不適切な名前はエラー
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self.__name = new_name

    def getName(self):
        print(self.__name)


class Pikachu(Pokemon):
    def attack(self):
        # 名前修飾によりself.__nameでアクセスできなくなるため、super().getName()からアクセス
        print(f"{super().getName()} の10万ボルト!")


class Zenigame(Pokemon):
    def attack(self):
        print(f"{super().getName()} のみずでっぽう!")


def main():
    pika = Pikachu("ピカチュウ", "でんき", "", 100)
    pika.attack()
    pika.changeName("テキセツ")
    pika.getName()
    pika.changeName("うんこ")
    pika.getName()


if __name__ == "__main__":
    main()
