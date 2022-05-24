unique = set()

for x in range(int(input())):
    name = input()
    unique.add(name)

[print(x) for x in unique]