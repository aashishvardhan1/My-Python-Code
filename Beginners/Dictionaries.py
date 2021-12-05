customer = {
    "Name": "John Smith",
    "Age": 30,
    "is_verified": True
}
print(customer["is_verified"])
# print(customer["birthdate"])  #Try this by removing Hash
print(customer.get("Name"))
print(customer.get("birthdate", "Jan 1 2000"))
# we can assign a default value here without getting errors

customer["Name"] = "Jack Smith"  # Updating a key in dictionary
print(customer.get("Name"))

print(customer.keys())
print(customer.values())


# Dictionaries are denoted with curly braces.