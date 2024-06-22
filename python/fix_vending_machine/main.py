import sys

from suica import Suica
from vending_machine import VendingMachine


def main():
    # Suicaの初期設定
    suica1 = Suica()
    # Suicaチャージ（100円以上の場合）
    try:
        suica1.charge(amount=500)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Suicaチャージ（100円未満の場合）： 処理が止まるのでコメントアウト
    # try:
    #     suica1.charge(amount=50)
    # except ValueError as e:
    #     print(e)
    #     sys.exit(1)

    # 自動販売機の初期設定
    vm = VendingMachine()

    print("=" * 60)
    print("初期の状態")
    print(f"Suica残高: {suica1.balance}")
    print(f"在庫状況: {vm.stock_info}")
    print(f"購入可能なドリンクリスト: {vm.get_available_drink_list(suica=suica1)}")
    print(f"売上金額: {vm.sales_amount}")
    print("=" * 60)

    # ドリンク購入
    print("ペプシ・モンスター・いろはすを1本ずつ購入")
    try:
        vm.purchase(suica=suica1, name="ペプシ")
        vm.purchase(suica=suica1, name="モンスター")
        vm.purchase(suica=suica1, name="いろはす")
    except ValueError as e:
        print(e)
        sys.exit(1)

    print("=" * 60)
    print(f"Suica残高: {suica1.balance}")
    print(f"在庫状況: {vm.stock_info}")
    print(f"売上金額: {vm.sales_amount}")
    print("=" * 60)

    # 在庫補充（対象ドリンクの場合）
    try:
        print("ペプシ5本補充")
        vm.add_stock("ペプシ", 5)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # 在庫補充（対象外ドリンクの場合）: 処理が止まるのでコメントアウト
    # try:
    #     print("ファンタ5本補充")
    #     vm.add_stock("ファンタ", 5)
    # except ValueError as e:
    #     print(e)
    #     sys.exit(1)

    print("=" * 60)
    print("最終結果")
    print(f"Suica残高: {suica1.balance}")
    print(f"在庫状況: {vm.stock_info}")
    print(f"売上金額: {vm.sales_amount}")
    print("=" * 60)


if __name__ == "__main__":
    main()
