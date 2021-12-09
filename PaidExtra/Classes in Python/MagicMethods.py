class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)
print(point)

# We can observe the change of output of line14 when we comment out the __str__ magic method.
# Output before: <__main__.Point object at 0x000001E313237CA0>
# Output after changing: (1,2)