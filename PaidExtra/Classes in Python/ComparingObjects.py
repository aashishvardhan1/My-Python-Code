class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)

# If we directly compare the instances without using magic methods like __eq__, then it 
# by default references the memory adresses of the instances. So we get False