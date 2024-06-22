class Juice:
    def __init__(self, name: str, price: int):
        self.__name: str = name
        self.__price: int = price

    @property
    def name(self) -> str:
        """ドリンク名を取得する"""
        return self.__name

    @property
    def price(self) -> int:
        """ドリンクの値段を取得する"""
        return self.__price


if __name__ == "__main__":
    pass
