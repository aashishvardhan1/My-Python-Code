def greet_user(first_name, last_name):   # first_name and last_name are parameters here!
    print(f"Hi {first_name} {last_name}!")
    print("Welcome Aboard")


print("Start")
greet_user("Aashish","Vardhan")     # Aashish and Vardhan are positional arguments here!
print("End")

greet_user(last_name="Vardhan", first_name="Aashish")
greet_user("Vardhan", last_name="Aashish")
# greet_user(first_name="Vardhan", "Aashish")   # Try this by removing Hash

#A positional argument after a keyword argument is not accepted. But viceversa is accepted
# Key word arguments are mainly used in functions where parameters are assigned to numericals.

# Key word arguments where position doesn't matter