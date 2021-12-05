numbers = [1,3,5,12,9,11,10]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

print(largest)