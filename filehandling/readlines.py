fp=open("newfile.txt",'r')
data=fp.readlines()

for i in data:
    word=i.split()
    print(word)