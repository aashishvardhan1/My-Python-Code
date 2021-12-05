import random

print(random.random())
print(random.randint(11, 40))

for i in range(2):
    print(random.random())
    print(random.randint(11,40))

# Random module is imported to generate random values. It has many methods.
print(' ')

comments = ['John', 'Mary', 'Bob', 'Mosh', 'Sarah']
random_comment_picker = random.choice(comments)

print(random_comment_picker)