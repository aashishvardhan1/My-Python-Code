import math

number = int(input("Enter Your Number: "))
fact = str(math.factorial(number))

for digit in reversed(fact):
    if digit != '0':
        print(digit)
        break
    else:
        pass

print("finish")