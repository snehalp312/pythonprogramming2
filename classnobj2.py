class employee:
    name=""
    age=0
    sal=0
    def get_info(self):
        self.deptno=10
        self.dname="Sales"
        return(self.dname,self.deptno)

# How to create object of class
obj=employee()
obj1=employee()
obj2=employee()

print(obj.get_info())
print(obj1.get_info())
print(obj2.get_info())
obj.sal=30000
obj.name="snehal"
obj.age=22
print(f"name={obj.name}\nage={obj.age}\nsalary={obj.sal}")