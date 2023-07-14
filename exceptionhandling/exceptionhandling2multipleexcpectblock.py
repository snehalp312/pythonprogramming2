print("out of try block")
try:
    a=5
    c=0
    b='a'
    # print(name)
    # print(int(b))
    print(a/c)

except TypeError:
    print("unupported operation")
except ValueError:
    print("valu error ")
except ZeroDivisionError:
    print("division by zero not alloweed")

except:
    print("Another error ")

print("Out of try except block")
