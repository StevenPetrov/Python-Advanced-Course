n = int(input())


def primary_diagonal(matrix):
    the_sum = 0
    l = []
    n = len(matrix)
    for x in range(n):
        the_sum += matrix[x][x]
        l.append(matrix[x][x])
    return the_sum, l


def secondary_diagonal(matrix):
    the_sum = 0
    ll = []
    n = len(matrix)
    for x in range(n):
        the_sum += matrix[x][n - x - 1]
        ll.append(matrix[x][n - x - 1])
    return the_sum, ll


matrix = []

for x in range(n):
    matrix.append([int(x) for x in input().split(', ')])

primary = primary_diagonal(matrix)
primary_sum, primary_list = primary
print(f'Primary diagonal: {", ".join([str(x) for x in primary_list])}. Sum: {primary_sum}')

secondary = secondary_diagonal(matrix)
secondary_sum, secondary_list = secondary
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_list])}. Sum: {secondary_sum}')
