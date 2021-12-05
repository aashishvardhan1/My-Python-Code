# For description of classes refer ClassesExplanation.txt file
class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()      # here point1 is a object or instance of the class point
point1.draw()
# as we defined the draw method/function earlier it can be accessed by the object created
# within the class 'Point'

point1.x = 10             # Here x is an attribute
point1.y = 20             # Here y is an attribute
print(point1.x)

point2 = Point()
# print(point2.x)         # Try this by removing Hash

# As point2 is a completely new object of the class 'Point', Attributes of point1
# cannot be implemented in point2.
