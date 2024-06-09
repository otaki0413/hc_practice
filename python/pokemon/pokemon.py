class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        print(f"{self.name} のこうげき!")


class Pikachu(Pokemon):
    def attack(self):
        super().attack()
        print(f"{self.name} の10万ボルト!")


class Zenigame(Pokemon):
    def attack(self):
        super().attack()
        print(f"{self.name} のみずでっぽう!")


def main():
    pika = Pikachu("ピカチュウ", "でんき", "", 100)
    zeni = Zenigame("ゼニガメ", "みず", "", 120)
    pika.attack()
    zeni.attack()


if __name__ == "__main__":
    main()
