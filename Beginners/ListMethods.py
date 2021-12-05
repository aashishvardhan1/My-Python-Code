numbers = [5,2,5,1,7,4]

numbers2 = numbers.copy()  #numbers2 list is printed at the end of the program

print(numbers.index(5))
print(numbers.count(5))
#print(numbers.index(39))  #Try this By removing Hash
print(5 in numbers)
print(39 in numbers)

numbers.sort()
numbers.reverse()
print(numbers)

numbers.append(20)
print(numbers)

numbers.insert(2,34)
print(numbers)

numbers.remove(7)
print(numbers)

numbers.pop()
print(numbers)

numbers.clear()
print(numbers)

print(numbers2)

#methods are that can be used after dot operator