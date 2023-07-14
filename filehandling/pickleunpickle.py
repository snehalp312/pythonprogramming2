import pickle
cars=["Audi","BMW","swift","MAruti Sujuki","scorpio"]
fileobj=open("mycar.pkl",'wb')
pickle.dump(cars,fileobj)
fileobj.close()

file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))