class A:
    def __init__(self):
        print("A class constructor invoked")

    def get_A(self,a):
        self.a=a
        return self.a
class B(A):
    def __init__(self):
        super().__init__()
        print("B class constructor invoked")


class C(B):
    def __init__(self):
        super().__init__()
        print("c class constructor invoked")

obj=C()