class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("eat")

''' Here,
Animal is a Parent or Base Class and
Mammal is a Chils or Sub Class'''

class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object)) # object is a default class that every class inherits
print(issubclass(Mammal, Animal))