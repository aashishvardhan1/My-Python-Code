def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 5, 8, 9))

# when number of inputs are not known