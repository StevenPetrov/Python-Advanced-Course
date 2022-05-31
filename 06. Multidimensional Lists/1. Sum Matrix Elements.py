rows, columns = [int(x) for x in input().split(', ')]

matrix = []
total_sum = 0

for x in range(rows):
    result = ([int(x) for x in input().split(', ')])
    matrix.append(result)
    total_sum += sum(result)

print(total_sum)
print(matrix)