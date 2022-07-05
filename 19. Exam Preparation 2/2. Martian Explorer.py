from collections import deque


def get_position(rover, direction):
    rover_row, rover_col = rover
    if direction == 'up':
        if rover_row - 1 < 0:
            future = 5, rover_col
        else:
            future = rover_row - 1, rover_col
    elif direction == 'down':
        if rover_row + 1 > 5:
            future = 0, rover_col
        else:
            future = rover_row + 1, rover_col
    elif direction == 'left':
        if rover_col - 1 < 0:
            future = rover_row, 5
        else:
            future = rover_row , rover_col - 1
    elif direction == 'right':
        if rover_col + 1 > 5:
            future = rover_row, 0
        else:
            future = rover_row, rover_col + 1

    return future

field = []
for row in range(6):
    field.append(input().split())

for row in range(6):
    for col in range(6):
        if field[row][col] == 'E':
            rover = (row, col)
metal = 0
water = 0
concrete = 0

commands = deque(input().split(', '))
broken = False

while commands and not broken:
    direction = commands.popleft()
    future = get_position(rover, direction)
    if field[future[0]][future[1]] == 'W':
        water += 1
        print(f'Water deposit found at {future}')
    elif field[future[0]][future[1]] == 'M':
        metal += 1
        print(f'Metal deposit found at {future}')
    elif field[future[0]][future[1]] == 'C':
        concrete += 1
        print(f'Concrete deposit found at {future}')
    elif field[future[0]][future[1]] == 'R':
        broken = True
        print(f'Rover got broken at {future}')
        break
    rover = future

if metal > 0 and water > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")