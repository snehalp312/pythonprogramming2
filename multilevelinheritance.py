class A:
    def get_A(self,a):
        self.a=a
        return self.a

class B(A):
    def get_B(self,b):
        self.b=b

class C(B):
    c=3
    def mul(self):
        self.result=self.get_A(2)*self.b*C.c
        return self.result

obj=C()
obj.get_B(3)
print(obj.mul())