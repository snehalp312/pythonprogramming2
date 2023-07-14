class A:
    def __init__(self,a):
        self.a=a

class B(A):
    def get_B(self,b):
        self.b=b

class C(B):
    c=9
    def mul(self):
        self.result=self.a* self.b*C.c
        print(self.result)

obj=C(10)
obj.get_B(3)
obj.mul()


