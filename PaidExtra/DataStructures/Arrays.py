from array import array

numbers = array('i', [1, 2, 3])
numbers.append(4)
numbers.insert(1,0)
numbers.pop()
numbers.remove(1)
print(numbers)

# Unlike lists, arrays store only a single dtype of objects that we specify through type code

# Arrays are only useful for large sequence of numbers and should be used only when
# performance issues are encountered.
