def square(number=int(input("Enter the Number: "))):
    result = number*number
    return result

print(square())

# By default any function returns the value NONE. So if we don't use
# return statement then the value None is printed on terminal along with
# the desired output.

def cube(digit=int(input("Enter the Digits: "))):
    result = digit * digit * digit
    print(result)

print(cube())

