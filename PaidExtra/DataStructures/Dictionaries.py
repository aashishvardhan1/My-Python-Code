# point = {"x":1, "y":2}
point = dict(x=1, y=2) # The above and this are same

print(point['x'])

point['x'] = 10
point['z'] = 20
print(point)

# print(point['a'])
 
# Instead of getting error we have 2 work arounds here, 
# first we can use if statement or we can use the get keyword here

if 'a' in point:
    print(point['a'])

print(point.get('a', 0)) # we are saying that if a is not there then give 0 as default output

del point['x'] # Deleting a key value pair
print(point) 

for key in point:
    print(key, point[key]) # Iterating through dictionaries

for key, value in point.items():
    print(key, value) # Printing pairs as tuples or unpacking tuples

# Dictionary is a data type with key value pairs