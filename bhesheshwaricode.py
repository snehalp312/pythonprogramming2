class vending_machine:
    coins = (5, 10, 20, 50, 100)
    def _init_(self,product_id,product_name,price):
        self.product_code=product_id
        self.product_name=product_name
        self.price=price

    def total_price(self):
        self.total_price=0

    def show_data(self):
        print("=========================")
        print(f"Product code:-{self.product_code}\n Product name:-{self.product_name}\n Product price:-{self.price}")
class user_input(vending_machine):
    def choice(self):
        choice = input("Please enter the product code you would like to purchase: ")


vending_machine_list=[]
#add instances to list
vending_machine_list.append(vending_machine(1,'coke',30))
vending_machine_list.append(vending_machine(2,'tea',15))
vending_machine_list.append(vending_machine(3,'coffee',40))
vending_machine_list.append(vending_machine(4,'chips',20))
vending_machine_list.append(vending_machine(5,'chocolate',10))

print("###### Welcome to my Vending Machine #######")
print("**All items below are readily available**")
for i in vending_machine_list:
    i.show_data()
c=user_input()
c.choice()