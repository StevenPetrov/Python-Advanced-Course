count = int(input())
names = set()
for _ in range(count):
    names.add(input())

[print(x) for x in names]