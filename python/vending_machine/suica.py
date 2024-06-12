class Suica:
    def __init__(self):
        self.balance = 500  # デフォルトのデポジット500円を設定

    def charge(self, amount):
        if amount >= 100:
            self.balance += amount
        else:
            raise ValueError("チャージ金額は100以上でなければいけません。")

    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    suica1 = Suica()
    suica1.charge(amount=500)

    try:
        suica1.charge(amount=50)
    except ValueError as e:
        print(e)

    balance = suica1.get_balance()
    print(balance)
