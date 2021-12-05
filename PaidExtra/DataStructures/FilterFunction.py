# after map function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered = list(filter(lambda item: item[1] >= 10, items)) # Similar to map function
print(filtered)