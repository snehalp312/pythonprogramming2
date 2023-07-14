class bank:

    def tunrover(self):
      print("Every bank has different turnover")

class hdfc(bank):
    super(bank)
    def tunrover(self):
        print("Hdfc bank has turnover around $24.102B")

class icici(bank):
    def tunrover(self):
        print("icici bank has turnover around $23.102B")

class SBI(bank):

    def tunrover(self):
        print("SBI bank has turnover around $28.102B")

obj1=bank()
obj2=hdfc()
obj3=icici()
obj4=SBI()

obj1.tunrover()
obj2.tunrover()
obj3.tunrover()
obj4.tunrover()