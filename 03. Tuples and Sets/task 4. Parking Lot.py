parking_lot = set()

for x in range(int(input())):
    direction, number = input().split(', ')
    if direction == 'IN':
        parking_lot.add(number)
    elif direction == 'OUT':
        parking_lot.remove(number)

if parking_lot:
    [print(x) for x in parking_lot]
else:
    print("Parking Lot is Empty")