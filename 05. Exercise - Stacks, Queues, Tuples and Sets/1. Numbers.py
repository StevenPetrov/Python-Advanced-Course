first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

lines = int(input())

for _ in range(lines):
    command = input()
    command = command.split()
    action = command[0]
    point = command[1]
    numbers = command[2:]
    if action == 'Add':
        if point == 'First':
            first = first.union(set([int(x) for x in numbers]))
        else:
            second = second.union(set([int(x) for x in numbers]))
    elif action == 'Remove':
        if point == 'First':
            first = first.difference(set([int(x) for x in numbers]))
        else:
            second = second.difference(set([int(x) for x in numbers]))
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
