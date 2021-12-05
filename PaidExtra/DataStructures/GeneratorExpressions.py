from sys import getsizeof

values1 = [x*2 for x in range(10)] # A List

# for x in values1:
#     print(x)

values = (x*2 for x in range(100000)) # A generator Object
print(getsizeof(values))

print(getsizeof(values1))

# We can say that a generator object is far more space efficient than lists with high no. of elements

# As generator objects doesn't store all the elements we cannot estimate the length of a Genarator object
# as a result, .len() method is not present in generator object

# Generator object is an iterable