try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid Age!")
except ZeroDivisionError:
    print("Age Cannot be Zero")
else:
    print("No Error is thrown.")

# If we want the same message for both the errors then we can specify both of them at the same except clause
# Note that if any one of the except blocks are excecuted, the others are ignored.