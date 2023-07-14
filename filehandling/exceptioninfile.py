user_info=input("Please add infromation")
try:
    with open("ff.txt","r") as fp:
        fp.write(user_info)
        print("data added succesfully")
        fp.seek(0)
        print(fp.read())
except Exception as e:
    print("There is a execption")


