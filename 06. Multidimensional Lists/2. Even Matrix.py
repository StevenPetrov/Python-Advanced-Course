rows = int(input())


matrix = []

for _ in range(rows):
    n = ([int(x) for x in input().split(', ')])
    matrix.append([x for x in n if x % 2 == 0])


print(matrix)