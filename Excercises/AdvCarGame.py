command = ''
car_started = False
car_stopped = True
while command != 'QUIT':
    command = input(">").upper()
    if command == 'HELP':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == 'START':
        if car_started:
            print("Car Already Started!")
        else:
            car_started = True
            car_stopped = False
            print("Car started. Ready to go..!")
    elif command == 'STOP':
        if car_stopped:
            print("Car is already Stopped!")
        else:
            car_stopped = True
            car_started = False
            print("Car stopped")
    elif command == 'QUIT':
        break
    else:
        print("I Don't Understand You")
