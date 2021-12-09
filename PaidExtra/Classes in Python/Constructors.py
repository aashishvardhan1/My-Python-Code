class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)
point.draw()
print(point.x)

# Here in the constructor self means that it shows the current instance.
# x and y are the attributes of the class Point that can be directly printed 
#on terminal as done in line 12.

# referencing to a robot(CLASS), it has all the parts such as motherboard, cameras etc. which 
#here are referenced as 'ATTRIBUTES' and the actions that it performs such as walking, speaking, 
#listening are referenced as 'FUNCTIONS'.