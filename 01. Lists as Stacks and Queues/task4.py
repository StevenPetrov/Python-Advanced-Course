from collections import deque

water = int(input())
ppl = deque()


while True:
    command = input()
    if command == "Start":
        break
    ppl.append(command)

while True:
    command = input()
    if command == "End":
        break
    elif command.isdigit():
        person = ppl.popleft()
        if int(command) <= water:
            print(f"{person} got water")
            water -= int(command)
        else:
            print(f"{person} must wait")
    elif command.startswith('refill '):
        command = command.split(" ")
        water_level = command[1]
        water += int(water_level)

print(f"{water} liters left")
