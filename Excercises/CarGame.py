command = ''
while command != 'QUIT':
    command = input(">").upper()
    if command == 'HELP':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == 'START':
        print("Car started. Ready to go..!")
    elif command == 'STOP':
        print("Car stopped")
    elif command == 'QUIT':
        break
    else:
        print("I Don't Understand You")
