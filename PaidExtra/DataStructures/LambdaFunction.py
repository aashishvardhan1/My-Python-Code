#Continued after sorting lists
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


items.sort(key=lambda item:item[1])
# Lambda syntax is lambda parameters:expression
print(items)