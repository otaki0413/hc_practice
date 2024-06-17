from suica import Suica
from juice import Juice


class VendingMachine:
    def __init__(self):
        self.__stock = {
            "ペプシ": [Juice(name="ペプシ", price=150) for _ in range(5)],
            "モンスター": [Juice(name="モンスター", price=230) for _ in range(5)],
            "いろはす": [Juice(name="いろはす", price=120) for _ in range(5)],
        }
        self.__sales_amount = 0

    def get_stock(self):
        """ドリンクの在庫状況を取得する"""
        stock_info = {}

        for name, juices in self.__stock.items():
            stock_info[name] = {"price": juices[0].get_price(), "quantity": len(juices)}

        return stock_info

    def add_stock(self, name, quantity):
        """在庫を追加する"""
        # 補充本数のチェック
        if quantity < 1:
            raise ValueError("補充する本数は、1以上の整数値を指定して下さい。")

        # 追加対象のドリンクかチェック
        if name not in self.__stock:
            raise ValueError(
                f"{name}は追加対象外のドリンクです。ペプシ、モンスター、いろはす から指定して下さい。"
            )

        # 対象ドリンクの値段取得
        price = self.__stock[name][0].get_price()

        # 既存のリストと、補充本数分のインスタンスを格納したリストを結合
        self.__stock[name].extend(
            [Juice(name=name, price=price) for _ in range(quantity)]
        )

    def get_available_drink_list(self, suica: Suica):
        """購入可能なドリンクリストを取得する"""
        available_drink_list = []

        for name, juices in self.__stock.items():
            # チャージ残高の不足と在庫の存在チェック
            if suica.get_balance() >= juices[0].get_price() and len(juices) > 0:
                available_drink_list.append(name)

        return available_drink_list

    def purchase(self, suica: Suica, name):
        """ドリンクを購入する"""
        # 購入対象のドリンクかチェック
        if name not in self.__stock:
            raise ValueError(
                f"{name}は自動販売機で扱っていません。ペプシ、モンスター、いろはすから選択して下さい。"
            )

        target_drink_list = self.__stock[name]

        # 対象ドリンクの在庫チェック
        if len(target_drink_list) < 1:
            raise ValueError(f"{name}の在庫がありません。")

        # 対象ドリンクの値段取得（在庫が0になると値段が取得できなくなるので、事前取得しておく）
        price = target_drink_list[0].get_price()

        # Suica支払い処理
        suica.pay(target_drink_list[0].get_price())

        # 在庫・売上の更新処理
        target_drink_list.pop()
        self.__sales_amount += price

    def get_sales_amount(self):
        """現在の売上金額を取得する"""
        return self.__sales_amount


if __name__ == "__main__":
    pass
