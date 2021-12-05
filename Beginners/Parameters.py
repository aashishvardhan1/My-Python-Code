def greet_user(first_name, last_name):   # first_name and last_name are parameters here!
    print(f"Hi {first_name} {last_name}!")
    print("Welcome Aboard")


print("Start")
greet_user("Aashish","Vardhan")     # Aashish and Vardhan are arguments here!
print("End")

greet_user("Vardhan", "Aashish")    # Positional arguments i.e, where position matters


# Here these parameters are called positional arguments
# i.e, if we change the position of the argument, the output changes.