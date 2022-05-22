

kids = input()
kids = kids.split()

n = int(input())
safe = n

current_position = 0

while len(kids) > 1:
    while True:
        n -= 1
        if n > 0:
            current_position += 1
            if current_position >= len(kids):
                current_position = 0
        else:
            break
    exit = kids.pop(current_position)
    print(f'Removed {exit}')
    n = safe
    if current_position >= len(kids):
        current_position = 0
print(f'Last is {kids[0]}')

