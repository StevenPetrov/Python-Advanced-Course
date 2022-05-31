rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

biggest_sum = 0
max_list = []

for row in range(rows - 1):
    for col in range(columns - 1):
        result = (matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1])
        if result > biggest_sum:
            biggest_sum = result
            max_list = [matrix[row][col],matrix[row][col+1],matrix[row+1][col],matrix[row+1][col+1]]

print(max_list[0],max_list[1])
print(max_list[2],max_list[3])
print(biggest_sum)