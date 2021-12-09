class Point:
    default_size = 2
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x}, {self.y})')

print(Point.default_size)

Point.default_size = 4

point = Point(1, 2)
point.draw()
print(point.default_size)
print(Point.default_size)

another = Point(5, 8)
another.draw()
print(another.default_size)

# here default_size is a class attribute which is same for all the instances of the class 
# while x and y are Instance attributes that vary from instance to instance.
# As a metaphor here, two different persons have different eye color(Instance attribute)
#but all the humans have only fixed number of eyes(Class Attribute) i.e., 2.