class Animal:
    def __init__(self):
        print("Animal Class")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        print("Mammal Class")
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)

# Constructor in Mammal class replaces the constructor in the base class i.e., 
#Animal class and this is called Method overriding

# super() keyword is used to access the constructor or the method that is getting 
#ovverrided in the base class. Then there will not be any replacements of the 
#methods, both can be execueted simultaneously.