class Suica:
    def __init__(self):
        self.__balance: int = 500  # デフォルトのデポジット500円を設定

    def charge(self, amount: int) -> None:
        if amount >= 100:
            self.__balance += amount
        else:
            raise ValueError("チャージ金額は100円以上でなければいけません。")

    def pay(self, amount: int) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("チャージ残高が不足しています。")

    @property
    def balance(self) -> int:
        return self.__balance


if __name__ == "__main__":
    pass
