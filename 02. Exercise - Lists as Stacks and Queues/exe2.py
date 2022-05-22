stack = []
cicle = input()

for _ in range(int(cicle)):
    command = input()
    if command.startswith('1'):
        command = command.split()
        stack.append(int(command[1]))
    elif command.startswith('2') and stack:
        stack.pop()
    elif command.startswith('3') and stack:
        print(max(stack))
    elif command.startswith('4') and stack:
        print(min(stack))

new = []
while stack:
    new.append(str(stack.pop()))

print(', '.join(new))
