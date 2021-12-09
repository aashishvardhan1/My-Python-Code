from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)
p2 = Point(x=1, y=2)
print(p2.y)
print(p1 == p2)

print(id(p2))

# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __eq__(self, other) -> bool:
#         return self.x == other.x and self.y == other.y


# We use the data classes when there is no requirement of any methods for a class that we are creating,
#instead the class only stores the data for us such as above point class.
# Here we take use of named tuples which is an in built class for storing data as tuples.