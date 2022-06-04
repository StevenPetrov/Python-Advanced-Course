matrix_size = int(input())

matrix = []
for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])


def if_valid(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    action, row, col, value = command
    row = int(row)
    col = int(col)
    value = int(value)
    if if_valid(row, col):
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
        continue

[print(*x, sep=' ') for x in matrix]