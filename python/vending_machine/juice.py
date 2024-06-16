class Juice:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        """ドリンク名を取得する"""
        return self.__name

    def get_price(self):
        """ドリンクの値段を取得する"""
        return self.__price


if __name__ == "__main__":
    pepci = Juice(name="ペプシ", price=150)
    print(pepci.get_price())
