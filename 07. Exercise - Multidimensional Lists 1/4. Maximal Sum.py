rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

biggest_sum = float('-inf')
max_list = []

for row in range(rows - 2):
    for col in range(columns - 2):
        result1 = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2]
        result2 = matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2]
        result3 = matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        max_result = result1 + result2 + result3
        if max_result > biggest_sum:
            biggest_sum = max_result
            max_list = [
                [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
            ]

print(f'Sum = {biggest_sum}')
for x in max_list:
    print(' '.join(str(y) for y in x))

