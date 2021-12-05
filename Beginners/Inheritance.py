class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def jump(self):
        print("Cats Jump")


dog = Dog()            # Inheritance can be seen here, although we didn't define the
dog.walk()               # method in class 'Dog' we can still access it because we inherited
                         # the 'Dog' Class to the class 'Mammal'

cat = Cat()
cat.walk()
cat.jump()