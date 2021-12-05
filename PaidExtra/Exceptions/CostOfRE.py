from timeit import timeit

code1 = '''
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as ex:
    pass
'''

code2 = '''
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calculate_xfactor(-1)

if xfactor is None:
    pass
'''

print(timeit(code1, number=10000))
print(timeit(code2, number=10000))

# Raising exceptions may take a lot of time. We can use if it is a simple application with few users. 
# Again just think before you Raise an exception. Raise only if it is necessary.