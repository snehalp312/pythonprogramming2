#subject marks result 1st clas=subject marks 3 to 4 subjects marks
# subject marks=m1,m2,m3,m4 ,sportsmarks= student class inherited by those two
class s_marks():
    def get_A(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        return m1,m2,m3

class sport_marks():
    def get_B(self,m4):
        self.m4=55
        return self.m4

class student(sport_marks,s_marks):
    def marks(self):
        self.marks=self.m1+self.m2+self.m3+self.m4
        self.per=self.marks/4
        print(self.marks)
        print(self.per)

obj=student()
obj.get_A(55,67,78)
obj.get_B(77)
obj.marks()





