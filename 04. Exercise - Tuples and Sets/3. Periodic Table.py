unique = set()

for x in range(int(input())):
    temp_set = set(input().split())
    unique = unique | temp_set

[print(x) for x in unique]

