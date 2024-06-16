from suica import Suica


class VendingMachine:
    def __init__(self):
        self.__stock = {
            "ペプシ": {"price": 150, "quantity": 5},
            "モンスター": {"price": 230, "quantity": 5},
            "いろはす": {"price": 120, "quantity": 5},
        }
        self.__sales_amount = 0

    def get_stock(self):
        """在庫を取得する"""
        return self.__stock

    def add_stock(self, name, quantity):
        """在庫を追加する"""
        if quantity < 1:
            raise ValueError("補充する本数は、1以上の整数値を指定して下さい。")

        if name in self.__stock:
            self.__stock[name]["quantity"] += quantity
        else:
            raise ValueError(
                f"{name}は追加対象外のドリンクです。ペプシ、モンスター、いろはす から指定して下さい。"
            )

    def get_available_drink_list(self, suica: Suica):
        """購入可能なドリンクリストを取得する"""
        available_drink_list = []

        for drink, drink_info in self.__stock.items():
            if (
                suica.get_balance() >= drink_info["price"]
                and drink_info["quantity"] > 0
            ):
                available_drink_list.append(drink)

        return available_drink_list

    def purchase(self, suica: Suica, name):
        """ドリンクを購入する"""
        # 購入対象のドリンクかチェック
        if name not in self.__stock:
            raise ValueError(
                f"{name}は自動販売機で扱っていません。ペプシ、モンスター、いろはすから選択して下さい。"
            )

        # 対象ドリンクの在庫チェック
        juice = self.__stock[name]
        if juice["quantity"] < 1:
            raise ValueError(f"{name}の在庫がありません。")

        # Suica支払い処理
        suica.pay(juice["price"])

        # 在庫・売上の更新処理
        juice["quantity"] -= 1
        self.__sales_amount += juice["price"]

    def get_sales_amount(self):
        """現在の売上金額を取得する"""
        return self.__sales_amount


if __name__ == "__main__":
    suica1 = Suica()
    suica1.charge(amount=500)
    print(f"Suica残高: {suica1.get_balance()}")

    vm = VendingMachine()
    print(f"在庫: {vm.get_stock()}")
    print(f"購入可能なドリンクリスト: {vm.get_available_drink_list(suica=suica1)}")

    # ドリンク購入
    try:
        vm.purchase(suica=suica1, name="モンスター")
    except ValueError as e:
        print(e)

    print(f"Suica残高: {suica1.get_balance()}")
    print(f"在庫: {vm.get_stock()}")
    print(f"売上金額: {vm.get_sales_amount()}")

    # 在庫補充（対象ドリンク）
    try:
        vm.add_stock("ペプシ", 5)
    except ValueError as e:
        print(e)
    print(vm.get_stock())

    # 在庫補充（対象外ドリンク）
    try:
        vm.add_stock("ファンタ", 5)
    except ValueError as e:
        print(e)
    print(vm.get_stock())

    print(f"Suica残高: {suica1.get_balance()}")
    print(f"在庫: {vm.get_stock()}")
    print(f"売上金額: {vm.get_sales_amount()}")
