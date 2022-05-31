n = int(input())


def primary_diagonal(matrix):
    the_sum = 0
    n = len(matrix)
    for x in range(n):
        the_sum += matrix[x][x]
    return the_sum


matrix = []

for x in range(n):
    matrix.append([int(x) for x in input().split()])

print(primary_diagonal(matrix))
