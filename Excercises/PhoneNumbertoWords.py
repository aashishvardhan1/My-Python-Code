phone = input("Phone: ")
numbers = {
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine"
}
output =''
for digits in phone:
    output += numbers.get(digits, "doesn't exist") + ' '

print(output)