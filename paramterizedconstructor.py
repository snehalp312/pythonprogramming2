class student:
    def __init__(self,name,m,n):
        self.a=m
        self.b=n
        self.name=name

    def show(self):
        print(f"{self.name}\t{self.a}\t{self.b}")

obj=student("sneha",23,34)
obj1=student("priya",56,67)
obj2=student("shweta",76,56)

obj.show()
obj1.show()
obj2.show()