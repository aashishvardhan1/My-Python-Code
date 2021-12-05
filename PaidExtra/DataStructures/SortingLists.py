numbers = [3, 51, 2, 8, 6]
new_numbers = sorted(numbers)
new_numbers2 = sorted(numbers, reverse=True)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
#sorted function doesn't effect the original list
#where as the list.sort method affects the original list
print(new_numbers)
print(new_numbers2)

#<------------------------------ New Case ----------------------------------->

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items.sort()
print(items)


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
# Note that sort doesn't take positional arguments it takes only keyword arguments
print(items)
