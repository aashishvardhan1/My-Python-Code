try:
    file = open("CleaningUp.py")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid Age!")
else:
    print("No Error is thrown.")
finally:
    file.close()

# 'Finally' key word is used to release the external resources that are being used in the process.
# 'Finally' block is executed after all the blocks irrespective of the result of above blocks.
# It is used to close files, database connections, network connections etc.