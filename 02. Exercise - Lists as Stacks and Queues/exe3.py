food = int(input())
orders = list(map(int,input().split()))

if orders:
    print(max(orders))
trigger = True

for x in range(len(orders)):
    first_order = orders[0]
    if food - first_order >= 0:
        food -= first_order
        orders.pop(0)
    else:
        trigger = False
        break

if trigger:
    print('Orders complete')
else:
    new = []
    while orders:
        new.append(str(orders.pop()))
    new.reverse()
    print(f"Orders left: {' '.join(new)}")
