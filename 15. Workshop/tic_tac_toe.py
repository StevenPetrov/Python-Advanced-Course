import time


def read_players():
    print('Hello to Tic Tac Toe game :)')
    time.sleep(1)
    player1 = input('Player one name: ')
    player2 = input('Player two name: ')

    while True:
        p1_sign = input(f'{player1} would you like to play with "X" or "O" ').upper()
        if p1_sign == 'X' or p1_sign == 'O':
            p2_sign = 'O' if p1_sign == 'X' else 'X'
            break

    return [(player1, p1_sign), (player2, p2_sign)]


def get_positions_mapping(board):
    result = {}
    idx = 1
    for row in range(len(board)):
        for col in range(len((board))):
            result[idx] = (row, col)
            idx += 1
    return result


def board_gen():
    board_size = 30
    board = []
    [board.append([None] * board_size) for x in range(board_size)]
    return board


def print_board_nums(board):
    print('This is the numeration of the board')
    idx = 1
    for row in range(len(board)):
        print('|', end='')
        for col in range(len((board))):
            print(f'  {idx}  |', end='')
            idx += 1
        print()


def print_board(board):
    for row in range(len(board)):
        print('|', end='')
        for col in range(len((board))):
            print(f'  {" " if board[row][col] is None else board[row][col]}  |', end='')
        print()


def check_for_win(player_sign, prow, pcol, board):
    won = True
    for col in range(len(board)):
        if board[prow][col] != player_sign:
            won = False
            break
    if won:
        return True
    won = True
    for row in range(len(board)):
        if board[row][pcol] != player_sign:
            won = False
            break
    if won:
        return True
    won = True
    for idx in range(len(board)):
        if board[idx][idx] != player_sign:
            won = False
            break
    if won:
        return True
    won = True
    for idx in range(len(board)):
        if board[idx][len(board) - 1 - idx] != player_sign:
            won = False
            break
    return won


def is_draw(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] is None:
                return False
    return True


def play_game(players, board, positions_mapping):
    print(f'{players[0][0]} starts first!')
    while True:
        try:
            player_name, player_sign = players[0]
            position = int(input(f'{player_name} choose a free position [1-9]: '))
            row, col = positions_mapping[position]
            if position not in positions_mapping:
                print(f'{position} is not a valid position!')
                continue
            if board[row][col] is not None:
                print(f'{position} is already taken!')
                continue
            board[row][col] = player_sign
            print_board(board)

            if check_for_win(player_sign, row, col, board):
                print(f"{player_name} won!")
                break

            if is_draw(board):
                print('Draw!')
                break

            players[0], players[1] = players[1], players[0]
        except Exception:
            pass


players = read_players()
board = board_gen()
print_board_nums(board)
positions_mapping = get_positions_mapping(board)
play_game(players, board, positions_mapping)

