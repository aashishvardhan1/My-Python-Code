class Point:
    def __init__(self, x, y, z):         # This is a constructor to intialise without
        self.x = x                    # any attribute
        self.y = y                    # Self is the reference to the any object we use
        self.z = z

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point = Point(10,20,30)
print(point.x)               # There is no point of defining another attribute x because it
print(point.y)               # is pre defined in the constructor. So, we should just pass the
print(point.z)               # values while craeting any object
