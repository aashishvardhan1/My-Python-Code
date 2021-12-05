# values = []
# for x in range(5):
#     values.append(x*2)

values = [x*2 for x in range(5)] # The above code is same as this (List Comprehension)

# Comprehension is not just limited to lists, it can be used upon sets and dictionaries also

values2 = {x*2 for x in range(5)} # Set

values3 = {x:x*2 for x in range(5)} # Dictionary

print(values3)

# Wondering that how we can comprehend tuples? Then:
# Refer GeneratorExpressions next for comprehension of tuples

