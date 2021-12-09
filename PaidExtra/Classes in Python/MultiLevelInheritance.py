class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird):
    pass


# Multi level inheritance makes the code very complex and is a bad practice.
# As seen in the above code, chicken is a bird but it cannot fly. This variations 
#can cause many confusions and errors in our code.

# As we have the animal class, it is not mandatory that we include eat method as all the animals can eat.
#We should just use inheritance when needed and that too avoiding the multi-level Inheritance.