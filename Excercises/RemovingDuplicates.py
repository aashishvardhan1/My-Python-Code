numbers = [5, 3, 7, 9, 2, 5, 7, 2, 9, 1, 2, 1, 3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)