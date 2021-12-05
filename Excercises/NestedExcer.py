numbers = [6, 2, 6, 2, 2]
for x_count in numbers:
    output = ''
    # for count in range(x_count):
    #     output += 'x'
    i = 0
    while i < x_count:
        output += 'x'
        i = i + 1
    print(output)