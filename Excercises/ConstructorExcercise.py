class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}.")


person1 = Person("Aashish Vardhan")
print(f'Name of person1 is {person1.name}')
person1.talk()

print(' ')

person2 = Person("John Smith")
print(f'Name of person2 is {person2.name}')
person2.talk()