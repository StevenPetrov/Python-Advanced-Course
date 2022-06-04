word = input().split("|")
clean = []

for x in reversed(word):
    z = x.split()
    for y in z:
        if y != " ":
            clean.append(y)

print(*clean, sep=' ')

