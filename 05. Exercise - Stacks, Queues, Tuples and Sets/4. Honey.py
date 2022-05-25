from collections import deque

actions = {
    '*': lambda a, b: abs(a * b),
    '/': lambda a, b: abs(a / b),
    '-': lambda a, b: abs(a - b),
    '+': lambda a, b: abs(a + b),

}

total_honey = 0

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
process = deque(input().split())

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    symbol = process.popleft()
    total_honey += actions[symbol](bee, nectar)

print(f'Total honey made: {total_honey}')
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")
