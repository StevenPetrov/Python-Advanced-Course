size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input().split()))

alice_row = 0
alice_col = 0
collected_bags = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'A':
            alice_col = col
            alice_row = row

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c)
}

while collected_bags < 10:
    matrix[alice_row][alice_col] = '*'

    command = input()
    new_row, new_col = directions[command](alice_row, alice_col)

    if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size:
        break

    alice_row, alice_col = new_row, new_col

    if matrix[alice_row][alice_col] == '.' or matrix[alice_row][alice_col] == '*':
        continue

    if matrix[alice_row][alice_col] == 'R':
        break

    collected_bags += int(matrix[alice_row][alice_col])

matrix[alice_row][alice_col] = '*'

if collected_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for x in matrix:
    print(*x, sep=' ')
