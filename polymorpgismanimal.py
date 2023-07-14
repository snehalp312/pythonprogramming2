class Animal:
    # petname=""
    def speak(self):
        print("animal")

class goat:
    def speak(self):
        print("aaaa")
        goat.petname="goty"
        print(goat.petname)

class cat:
    def speak(self):
        print("meowww")
        cat.petname = "catty"
        print(cat.petname)

class dog:
    def speak(self):
        print("bhowwww")
        dog.petname = "doggy"
        print(dog.petname)

obj1=Animal()
obj2=goat()
obj3=cat()
obj4=dog()
obj1.speak()
obj2.speak()
obj3.speak()
obj4.speak()

