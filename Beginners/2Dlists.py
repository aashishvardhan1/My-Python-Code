matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[1][2] = 20
print(matrix[1][2])
print(matrix)
print(' ')

for row in matrix:
    for item in row:
        print(item)