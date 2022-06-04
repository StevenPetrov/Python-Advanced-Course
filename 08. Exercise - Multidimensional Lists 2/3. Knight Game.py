matrix_size = int(input())

matrix = []
for _ in range(matrix_size):
    matrix.append(list(input()))

removed_knights = 0
def find_count(row,col,matrix):
    count = 0
    moves = [
        [row + 2,col - 1],
        [row + 2,col + 1],
        [row + 1,col - 2],
        [row + 1,col + 2],
        [row - 2,col - 1],
        [row - 2,col + 1],
        [row - 1,col - 2],
        [row - 1,col + 2]
    ]
    for r, c in moves:
        if 0 <= r < len(matrix) and  0 <= c < len(matrix) and matrix[r][c] == "K":
            count += 1

    return count


while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(matrix_size):
        for col in range(matrix_size):
            type = matrix[row][col]
            if type == '0':
                continue
            count = find_count(row,col,matrix)
            if count > best_count:
                best_count = count
                knight_col = col
                knight_row  = row

    if best_count == 0:
        break

    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)
