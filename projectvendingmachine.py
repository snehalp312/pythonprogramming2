class VendingMachine:
    def __init__(self):
        self.items = {
            'mazaa': 15,
            'chips': 10,
            'kitkat': 5,
            'munch':20,
            'kurkure':5,
            'lolipop':5,
            'fruity':10,
            'lassi':20
        }
        self.balance = 0

    def display_items(self):
        print("Available Items:")
        print("*******************")
        for item, price in self.items.items():
            print(f"{item}: {price}")
            print("__________________")

    def insert_coin(self, coin):
        l1_coins=[5,10,20,50]
        if coin not in l1_coins:
            print("Invalid coin.")
            return

        self.balance += coin

    def purchase_item(self, item):
        if item not in self.items:
            print("Invalid item.")
            return

        price = self.items[item]
        if self.balance < price:
            print("Insufficient balance.")
            return

        change = self.balance - price
        coins = self.calculate_coins(change)

        print(f"Take your {item}. Enjoy!!!!!!!!!!")
        if change > 0:
            print(f"Plzz collect your change :{change}")
            print("coins")
            for coin, count in coins.items():
                print(f"{coin}:{count}")

        self.balance = 0

    def calculate_coins(self, change):
        coin_values = [5,10,20,50]
        coins = {}

        for coin in coin_values:
            count = change // coin
            change %= coin
            if count > 0:
                coins[coin] = int(count)

        return coins
    def showbls(self,bls):
        self.bls=self.balance
        print({self.balance})

def main():
    vending_machine = VendingMachine()

    print("Welcome to the Vending Machine!")
    vending_machine.display_items()

    while True:
        print("\nWelcome to Vending Machine!!!!!!!!!!!")
        print("1. Insert Coin")
        print("2. Purchase Item")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            coin = int(input("Enter the coin amount (5, 10, 20,50): "))
            vending_machine.insert_coin(coin)
        elif choice == '2':
            item = input("Enter the item to purchase: ")
            vending_machine.purchase_item(item)
        elif choice == '3':
            print("Thank you for using the vending machine. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
