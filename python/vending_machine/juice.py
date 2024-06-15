class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == "__main__":
    pepci = Juice(name="ペプシ", price=150)
    print(pepci.price)
