point1 = (1, 2)
point2 = 1, 2
point3 = 1
point4 = 1,
print(type(point1))
print(type(point2))
print(type(point3))
print(type(point4))

points = (1, 2) + (3, 4)
points2 = (1, 2) * 3

print(points)
print(points2)

# We need not to use brackets while declaring a tuple

point5 = tuple([1, 2, 3])
point6 = tuple("Aashish Vardhan")

print(point5)
print(point6)

x, y, z = point5 # unpacking of tuples
if 1 in point5:
    print("Exists")
