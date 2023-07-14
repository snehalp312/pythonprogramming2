class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

student_list=[]

student_list.append(student("sneha",1))
student_list.append(student("neha",2))
student_list.append(student("shamal",3))
student_list.append(student("gargi",4))
student_list.append(student("vani",5))

# accesing all instances from list
for obj in student_list:
    print(obj.name,obj.rollno)

# for indivijual name printing
print(student_list[0].name)
print(student_list[0].rollno)
