from suica import Suica


class VendingMachine:
    def __init__(self):
        self.stock = {"ペプシ": {"price": 150, "quantity": 5}}

    def get_stock(self):
        return self.stock


if __name__ == "__main__":
    suica1 = Suica()
    suica1.charge(amount=200)

    vm = VendingMachine()
    print(f"在庫: {vm.get_stock()}")
