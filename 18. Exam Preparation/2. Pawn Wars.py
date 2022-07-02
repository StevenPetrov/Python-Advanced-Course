from collections import deque

board = []
for _ in range(8):
    board.append([x for x in input().split()])


def validate(matrix):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'w':
                white = row, col
            if board[row][col] == 'b':
                black = row, col
    return white, black


current_player, other_player = validate(board)













#
#
# def check_mate(board, player):
#     winner = False
#     row_attack, col_attack = player
#     if player == white:
#         for row in range(len(board)):
#             for col in range(len(board)):
#                 if (board[row_attack + 1][col_attack - 1] == 'b' or board[row_attack + 1][col_attack + 1] == 'b'):
#                     winner = True
#     elif player == black:
#         for row in range(len(board)):
#             for col in range(len(board)):
#                 if (board[row_attack - 1][col_attack - 1] == 'b' or board[row_attack - 1][col_attack + 1] == 'b'):
#                     winner = True
#         if winner:
#             return player
#
#
# while True:
#     player = order.popleft()
#     row_attack, col_attack = player
#
#     if not check_mate(board, player):
#         if player == white:
#             board[row_attack][col_attack], board[row_attack - 1][col_attack] = board[row_attack - 1][col_attack], \
#                                                                                board[row_attack][col_attack]
#             white = (row_attack - 1, col_attack)
#             player = white
#             [print(*x, sep=' ') for x in board]
#             print()
#         else:
#             board[row_attack][col_attack], board[row_attack + 1][col_attack] = board[row_attack + 1][col_attack], \
#                                                                                board[row_attack][col_attack]
#             black = (row_attack + 1, col_attack)
#             player = black
#             [print(*x, sep=' ') for x in board]
#             print()
#     else:
#         print(f"Game over! {player} win, capture on {board[row_attack + 1][col_attack]}.")
#         break
#     row_attack, col_attack = player
#     if (player == white and row_attack == 0) or (player == black and row_attack == 8):
#         print(f"Game over! {player} pawn is promoted to a queen at {board[row_attack + 1][col_attack]}.")
#         break
#
#     order.append(player)
