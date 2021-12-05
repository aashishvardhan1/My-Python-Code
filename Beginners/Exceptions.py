try:
    age = int(input("Age: "))
    print(age)
    income = 20000
    risk = income/age
    print(risk)
except ZeroDivisionError:                   # Except block for Zero Division Error
    print("Age Cannot Be Zero!")
except ValueError:                          # Except block for Value Error
    print("Invalid Characters Entered!")