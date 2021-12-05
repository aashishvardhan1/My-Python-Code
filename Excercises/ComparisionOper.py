name = input("Enter Your Name: ")

if len(name) < 3:
    print("Name must be at least 3 Characters Long!")
    print("Try Again!")
elif len(name) > 50:
    print("Name Cannot exceed 50 Characters!")
    print("Try Again!")
else:
    print("Name Looks Good!")
    print(f'Welcome on board {name}')