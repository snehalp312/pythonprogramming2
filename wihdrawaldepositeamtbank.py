class bank:
    def __init__(self,acctype,accno,name,amt):
        self.ac_type=acctype
        self.ac_no=accno
        self.ac_ame=name
        self.amount=amt

    def withdrawal(self):
        self.wit_amt=int(input("How much amt u wantto withdraw"))
        self.amount=self.amount-self.wit_amt

    def show_statement(self):
        print(f"{self.ac_no}\t{self.ac_ame}\t{self.ac_type}\t{self.amount}")
    def depo_smt(self):
        self.de_amt=int(input("Enter amt u want to deposite"))
        self.amout=self.amount+self.de_amt



obj1=bank(1,"sneha","saving",45000)
obj2=bank(2,"neha","current",65000)
obj1.withdrawal()
obj1.show_statement()
obj2.depo_smt()
obj2.show_statement()
