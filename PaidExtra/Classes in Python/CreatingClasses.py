class Point:
    def draw(self):
        print('Draw')


point = Point()
point.draw()

print(isinstance(point, Point))
print(isinstance(point, int))