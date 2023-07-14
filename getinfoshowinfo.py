class student:
    institute_name="ITP"

    def get_info(self,stno,sname,p1,p2,p3):
        self.m1=p1
        self.m2 = p2
        self.m3 = p3
        self.stno=stno
        self.sname=sname

    def show_info(self):
        print(f"{self.stno}\t{self.sname}\t{self.m1}\t{self.m2}\t{self.m3}")

    def cal_result(self):
        self.total=self.m1+self.m2+self.m3
        self.per=self.total/3

obj=student()
obj1=student()

obj.get_info(1,"sneha",67,78,89)
obj1.get_info(2,"neha",77,90,79)

obj.cal_result()
obj.show_info()

obj1.cal_result()
obj1.show_info()