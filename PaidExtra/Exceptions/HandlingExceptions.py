try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid Age!")
    print(ex)
    print(type(ex))
else:
    print("No Error is thrown.")
print("Execution Continues")

# Else block is executed only when try block executes sucessfully, similar to for-else loops.