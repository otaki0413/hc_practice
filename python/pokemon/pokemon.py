class Pokemon:
    def __init__(self, name, type1, type2, hp, mp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.mp = mp

    def attack(self):
        print(f"{self.name} のこうげき!")


def main():
    poke: Pokemon = Pokemon()
    print(poke.name)
    print(poke.type1)
    print(poke.mp)
    poke.attack()


if __name__ == "__main__":
    main()
