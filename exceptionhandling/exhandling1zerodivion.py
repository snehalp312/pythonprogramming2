print("welcome to exception handling")
n1=9
n2=34
s=n1+n2
print("sum:=",s)
try:
    a=int(input("enter value of a"))
    b = int(input("enter value of b"))
    print(a/b)
except:
    print("some error occured")

else:
    print("out of try expect block")