from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted_water = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()
    while True:
        if cup <= bottle:
            wasted_water += bottle - cup
            break
        else:
            cup -= bottle
        bottle = bottles.pop()

if not cups:
    bottles = [str(x) for x in bottles]
    print(f'Bottles: {" ".join(bottles)}')
    print(f'Wasted litters of water: {wasted_water}')
if not bottles:
    cups = [str(x) for x in cups]
    print(f'Cups: {" ".join(cups)}')
    print(f'Wasted litters of water: {wasted_water}')