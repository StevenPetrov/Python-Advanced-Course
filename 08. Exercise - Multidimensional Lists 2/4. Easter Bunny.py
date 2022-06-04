field = int(input())

matrix = []

for _ in range(field):
    matrix.append(list(input().split()))
best_move = float('-inf')
direction = ''
bunny_col = 0
bunny_row = 0
for row in range(field):
    for col in range(field):
        if matrix[row][col] == 'B':
            bunny_col = col
            bunny_row = row

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c)
}

best_path = []

for move in directions:
    current_path = []
    moves = 0
    row, col = directions[move](bunny_row,bunny_col)

    while 0 <= row < field and 0 <= col < field and matrix[row][col] != 'X':
        moves += int(matrix[row][col])
        current_path.append([row,col])
        row, col = directions[move](row, col)

    if moves > best_move and current_path:
        best_move = moves
        direction = move
        best_path = current_path
print(direction)
print(*best_path, sep='\n')
print(best_move)
