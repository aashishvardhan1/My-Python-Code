# After Lambda Function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

x = list(map(lambda item: item[1], items))
# we are using list method as map returns another iterable object
print(x)