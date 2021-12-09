class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()

# The intrepetor initially checks the first base class for the method greet. 
# As we have that it runs that method and terminates our program.

# Multiple inheritance can become a hectic task if not used properly. If someone 
# changes the order of our base classes then automatically the behaviour of our 
# program changes.

# This is something that could ruin our project. So it is better to lower the 
# usage of both multilevel and nultiple inheritance. If both are not used properly,
# then some classes could inherit the properties that they shouldn't, 
# Like the chicken could fly in the previous example.


# The below code is a perfect usage of multiple inheritance
# We have a flyer a swimmer and a flying fish can do both the tasks.


class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass


