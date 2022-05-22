from collections import deque

gas_stations = int(input())
petrols = deque()

for _ in range(gas_stations):
    petrols.append([int(x) for x in input().split()])


for x in range(gas_stations):
    tank = 0
    failed = False
    for fuel, distance in petrols:
        tank = tank + fuel - distance
        if tank < 0 :
            failed = True
            break
    if failed:
        petrols.append(petrols.popleft())
    else:
        print(x)
        break

