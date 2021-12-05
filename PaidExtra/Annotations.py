# Annotations are that describe the returning or which type of a variable it is

def increment(number: int , by: int) -> tuple:
    return (number, number + by)     # In python functions we can return multiple values at a time


print(increment(2, by=5))            # Keyword arguments

# As the return value contains two values it is being printed as a tuple but not as an integer

#Syntax of the annotations is variable: type