from suica import Suica


class VendingMachine:
    def __init__(self):
        self.stock = {"ペプシ": {"price": 150, "quantity": 5}}
        self.sales_amount = 0

    def get_stock(self):
        return self.stock

    def can_purchase(self, suica: Suica):
        balance = suica.get_balance()
        return balance >= self.stock["ペプシ"]["price"]

    def purchase(self, suica: Suica):
        juice = self.stock["ペプシ"]
        if juice["quantity"] < 1:
            raise ValueError(f"{juice}の在庫がありません。")

        # Suica支払い処理と在庫・売上更新
        suica.pay(juice["price"])
        juice["quantity"] -= 1
        self.sales_amount += juice["price"]

    def get_sales_amount(self):
        return self.sales_amount


if __name__ == "__main__":
    suica1 = Suica()
    suica1.charge(amount=100)
    print(f"Suica残高: {suica1.get_balance()}")

    vm = VendingMachine()
    print(f"在庫: {vm.get_stock()}")

    try:
        vm.purchase(suica=suica1)
    except ValueError as e:
        print(e)

    print(f"Suica残高: {suica1.get_balance()}")
    print(f"在庫: {vm.get_stock()}")
    print(f"売上金額: {vm.get_sales_amount()}")
