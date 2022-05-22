from collections import deque

l = deque(input().split())

n = []

for x in range(len(l)):
    n.append(l.pop())

print(' '.join(n))

# l = input()
#
# l = l[::-1]
#
# print(l)
