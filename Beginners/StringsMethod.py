course = "Python for Beginners"
print(len(course))
print(course[:8])
print(course[2:])
print(course[:])
#Print and len are functions that can be used in all types not especially for strings
#There are specifically some methods for Strings, that can be acessed using dot operator.
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('o'))
print(course.replace('Beginners','Absolute Beginners'))
print(course)
print('Python' in course)
print('python' in course)
