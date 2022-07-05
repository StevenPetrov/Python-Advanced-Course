from collections import deque

player1, player2 = input().split(', ')

size = 6
board = []

for row in range(size):
    board.append(input().split())

wall_1 = 0
wall_2 = 0

while True:

    player1_coords = input()
    if wall_1 < 1:
        row, col = int(player1_coords[1]), int(player1_coords[4])
        if board[row][col] == 'E':
            print(f"{player1} found the Exit and wins the game!")
            break
        elif board[row][col] == 'T':
            print(f"{player1} is out of the game! The winner is {player2}." )
            break
        elif board[row][col] == 'W':
            print(f"{player1} hits a wall and needs to rest.")
            wall_1 = 2
    wall_2 -= 1


    player2_coords = input()
    if wall_2 < 1:
        row, col = int(player2_coords[1]), int(player2_coords[4])
        if board[row][col] == 'E':
            print(f"{player2} found the Exit and wins the game!")
            break
        elif board[row][col] == 'T':
            print(f"{player2} is out of the game! The winner is {player1}.")
            break
        elif board[row][col] == 'W':
            wall_2 = 2
            print(f"{player2} hits a wall and needs to rest.")
    wall_1 -= 1
