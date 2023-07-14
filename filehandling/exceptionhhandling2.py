import pickle
cars={'audi':2,'BMW':3,'Maruti Suzuki':4}
fileobj=open('mycar.pkl','wb')
pickle.dump(cars,fileobj)
fileobj.close()

#unpickle
file='mycar.pkl'
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))
