# class VendingMachine:
#     def __init__(self):
#         self.items = {
#             'Coke': 1.50,
#             'Chips': 1.00,
#             'Candy': 0.75
#         }
#         self.balance = 0.0
#
#     def display_items(self):
#         print("Available Items:")
#         for item, price in self.items.items():
#             print(f"{item}: ${price}")
#
#     def insert_money(self, amount):
#         self.balance += amount
#
#     def purchase_item(self, item):
#         if item not in self.items:
#             print("Invalid item.")
#             return
#
#         price = self.items[item]
#         if self.balance < price:
#             print("Insufficient balance.")
#             return
#
#         print(f"Dispensing {item}. Enjoy!")
#         change = self.balance - price
#         if change > 0:
#             print(f"Your change: ${change}")
#         self.balance = 0.0
#
#     def display_balance(self):
#         print(f"Current balance: ${self.balance}")
#
#
# def main():
#     vending_machine = VendingMachine()
#
#     while True:
#         print("\n=== Vending Machine ===")
#         print("1. Display Items")
#         print("2. Insert Money")
#         print("3. Purchase Item")
#         print("4. Display Balance")
#         print("5. Exit")
#
#         choice = input("Enter your choice (1-5): ")
#
#         if choice == '1':
#             vending_machine.display_items()
#         elif choice == '2':
#             amount = float(input("Enter the amount to insert: $"))
#             vending_machine.insert_money(amount)
#         elif choice == '3':
#             item = input("Enter the item to purchase: ")
#             vending_machine.purchase_item(item)
#         elif choice == '4':
#             vending_machine.display_balance()
#         elif choice == '5':
#             print("Thank you for using the vending machine. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if __name__ == '__main__':
#     main()
#


class VendingMachine:
    def __init__(self):
        self.items = {
            'Coke': 150,
            'Chips': 100,
            'Candy': 75,
        }
        self.balance = 0

    def display_items(self):
        print("Available Items:")
        for item, price in self.items.items():
            print(f"{item}: {price}")

    def insert_coin(self, coin):
        if coin not in [5, 10, 20, 50, 100]:
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

        print(f"Dispensing {item}. Enjoy!")
        if change > 0:
            print(f"Change:{change}")
            print("Coins:")
            for coin, count in coins.items():
                print(f"{coin}:{count}")

        self.balance = 0

    def calculate_coins(self, change):
        coin_values = [100, 50, 20, 10, 5]
        coins = {}

        for coin in coin_values:
            count = change // coin
            change %= coin
            if count > 0:
                coins[coin] = int(count)

        return coins


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
            coin = int(input("Enter the coin amount (5, 10, 20, 50, or 100 cents): "))
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
