numbers = [1, 1, 2, 3, 3, 4]
first = set(numbers)
second = {1, 6}
second.add(5)
second.remove(5)
print(len(second))
print(first)

print(first | second) # Union Operation b/w 2 sets
print(first & second) # Intersection operation b/w 2 sets
print(first - second) # Difference of 2 sets
print(first ^ second) # Opposite to intersection

if 1 in first:
    print('Yes')

# Unlike lists, Sets doesn't support indexing as elements in sets are not in a particular order