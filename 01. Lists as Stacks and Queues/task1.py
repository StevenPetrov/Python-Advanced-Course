front = input()

stack = []
reversed = ''
for x in front:
    stack.append(x)

while stack:
    reversed += stack.pop()

print(reversed)
