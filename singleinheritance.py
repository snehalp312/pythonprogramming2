class bank:
    def cust_info(self,name,accno,balance,actype):
        self.name=name
        self.accno=accno
        self.balance=balance
        self.actype=actype

    # def __init__(self,name,accno,balance,actype):
    #     self.name=name
    #     self.accno=accno
    #     self.balance=balance
    #     self.actype=actype

class customer(bank):
    cust_add="pune"
    def show_cust_info(self):
        print(f"{self.accno} {self.name} {customer.cust_add}")

c=customer()
c.cust_info("sneha",101,20000,"saving")
c.show_cust_info()
#
# c=customer("neha",102,67000,"current")
# c.show_cust_info()