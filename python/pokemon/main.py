from pokemon import Pikachu
from player import Player


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
