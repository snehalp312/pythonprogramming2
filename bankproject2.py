class BANK:
    def init(self, cx_id, cx_name, acc_type, branch_name, cx_address, balance):
        self.cx_id = cx_id
        self.cx_name = cx_name
        self.acc_type = acc_type
        self.branch_name = branch_name
        self.cx_address = cx_address
        self.balance = balance

    def display(self):
        print(f"Customer ID: {self.cx_id}")
        print(f"Customer Name: {self.cx_name}")
        print(f"Account Type: {self.acc_type}")
        print(f"Branch Name: {self.branch_name}")
        print(f"Customer Address: {self.cx_address}")
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance+ amount
        print(f"Balance_after_deposit: {self.balance}")

    def withdrawl(self, withdrawl_amount):
        if self.balance >= withdrawl_amount:
            self.balance = self.balance - withdrawl_amount
            print(f"Withdrawal Successful! Balance_after_withdrawl: {self.balance}")
        else:
            print("check Balance!")

    def loan(self, principle_amount, intrest, time_period):
        total_amount = (principle_amount * intrest * time_period) / 100
        emi = total_amount / time_period
        print(f"Total loan_Amount: {total_amount}")
        print(f"EMI/month: {emi}")


class HDFC(BANK):
    def display1(self,bank_name):
        self.bank_name = bank_name
        print(self.bank_name)




class AXIX(BANK):
    def display1(self,bank_name):
        self.bank_name = bank_name
        print(self.bank_name)



class ICICI(BANK):
    def display1(self,bank_name):
        self.bank_name = bank_name
        print(self.bank_name)


a = HDFC(111, "prashik", "saving", "hadapsar_branch", "pune", 0)
a.display1("HDFC BANK")
a.display()
a.deposit(10000)
a.withdrawl(5000)
a.loan(10000, 10, 12)
print()
print()
b = AXIX(222, "sanket", "current", "mg_road_branch", "mumbai", 10000)
b.display1("AXIX BANK")
b.display()
b.deposit(15000)
b.withdrawl(3000)
b.loan(20000, 12, 24)
print()
print()
c = ICICI(333, "parag", "saving", "magarpata_branch", "nagpur", 0)
c.display1("ICICI BANK")
c.display()
c.deposit(20000)
c.withdrawl(8000)
c.loan(15000, 8, 18)