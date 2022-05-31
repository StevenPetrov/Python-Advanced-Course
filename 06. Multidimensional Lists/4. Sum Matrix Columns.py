rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

matrix_sums = [0] * columns

for x in range(rows):
    for y in range(columns):
        matrix_sums[y] += matrix[x][y]

[print(x) for x in matrix_sums]
