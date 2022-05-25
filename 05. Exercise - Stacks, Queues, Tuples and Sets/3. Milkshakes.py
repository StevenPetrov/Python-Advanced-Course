from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cup_milks = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while milkshakes < 5 and chocolates and cup_milks:
    work_choco = chocolates.pop()
    work_cup_milk = cup_milks.popleft()

    if work_choco <= 0 and work_cup_milk <= 0:
        continue

    if work_choco <= 0:
        cup_milks.appendleft(work_cup_milk)
        continue
    if work_cup_milk <= 0:
        chocolates.append(work_choco)
        continue

    if work_choco == work_cup_milk:
        milkshakes += 1

    else:
        cup_milks.append(work_cup_milk)
        chocolates.append(work_choco-5)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cup_milks:
    print(f"Milk: {', '.join([str(x) for x in cup_milks])}")
else:
    print("Milk: empty")
