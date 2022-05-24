l = [int(x) for x in input().split()]
target_number = int(input())

unique = set()
iterations_count = 0
for x in l:
    for y in l:
        iterations_count += 1
        if x + y == target_number:
            print(f'{x} + {y} = {target_number}')
            unique.add((x, y))
print(f'Iterations done: {iterations_count}')
[print(x) for x in unique]