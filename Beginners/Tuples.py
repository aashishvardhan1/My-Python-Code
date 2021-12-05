numbers1 = [1, 2, 3, 4, 5]  # List
numbers2 = (1, 2, 3, 4, 5)  # Tuple

# Using dot operator check difference between methods of lists and tuples

numbers1.append(2)
numbers2.count(1)

#numbers2[1] = 20  # Try this by removing Hash

#tuples are those we cannot modify,insert,remove or clear the objects in tuples
#we use tuples where we don't want to change the values in the list throughout our program
#So, when we try to update the value of a tuple it will result in an error.
#we also cannot access the append method after the dot operator.