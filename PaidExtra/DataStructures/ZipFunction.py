list1 = [1, 2, 3]
list2 = [10, 20, 30]

y = list(zip("abc",list1, list2)) # any iterables can be passed
print(y)

# To combine elements of two lists by taking their corresponding elements and making them
# into tuples