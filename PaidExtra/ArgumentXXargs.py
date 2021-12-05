def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name='Aashish')


#in **args we pass keyword arguments than just normal arguments.
# here if we print the function a dictionary is returned.