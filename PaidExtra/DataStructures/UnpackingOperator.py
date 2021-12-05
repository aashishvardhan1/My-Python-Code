numbers = [1, 2, 3, 4]

print(numbers)
print(*numbers) # Unpacked list using asterisk

values = [*range(5), *"HelloWorld"] # We can directly unpack the iterables
print(values)

first = [1, 2]
second = [3]
values2 = [*first, "R", *second, *"HelloWorld"]

# We can also unpack the dictionaries by using '**' operator

dict1 = {"x" : 1}
dict2 = dict(x=10, y=20)

combined_dict = {**dict1, **dict2, "z":30}
print(combined_dict)

# Finally we use the unpacking operator take out individual element from any iterable