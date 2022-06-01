def primary_diagonal(matrix):
    the_sum = 0
    n = len(matrix)
    for x in range(n):
        the_sum += matrix[x][x]
    return the_sum


def secondary_diagonal(matrix):
    the_sum = 0
    n = len(matrix)
    for x in range(n):
        the_sum += matrix[x][n - x - 1]
    return the_sum


n = int(input())

matrix = []

for x in range(n):
    matrix.append([int(x) for x in input().split()])

result = abs(primary_diagonal(matrix) - secondary_diagonal(matrix))
print(result)