try:
    with open("WithStatement.py") as file:
        print("File Opened")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid Age!")
else:
    print("No Error is thrown.")


# When we use the with method, python automatically releases/ closes the external resources.
# In other words, no need to use finally block when we use the with method.

# If Magic methods such as __exit__ and __enter__ are there for a file then "with" can be used.