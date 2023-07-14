with open("C:\\Users\\pp\\Desktop\\ITPRENEURallnotespdf\\test90.txt",'r+') as fp:
    fp.write("Django is the popular framework used in python")
    fp.seek(0)
    print(fp.tell())
    print(fp.read())

with open("test1.txt",'r') as fp2:
    fp2.seek(4)
    fp2.tell()