class Suica:
    def __init__(self):
        self.__balance = 500  # デフォルトのデポジット500円を設定

    def charge(self, amount):
        if amount >= 100:
            self.__balance += amount
        else:
            raise ValueError("チャージ金額は100円以上でなければいけません。")

    def pay(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("チャージ残高が不足しています。")

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    pass
