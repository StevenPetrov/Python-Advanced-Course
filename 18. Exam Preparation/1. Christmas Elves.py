from collections import deque

elves_energy = deque([int(x) for x in input().split(' ')])
boxes_left = deque([int(x) for x in input().split(' ')])

elf_num = 0
toy_count = 0
energy_used = 0

while elves_energy and boxes_left:
    no_energy = False
    elf_num += 1
    elf = elves_energy.popleft()
    if elf < 5:
        continue
    box = boxes_left.pop()

    if elf_num % 15 == 0:
        if elf >= box * 2:
            elf -= box * 2
            energy_used += box * 2
            elves_energy.append(elf)
        else:
            no_energy = True

    elif elf_num % 3 == 0:
        if elf >= box * 2:
            toy_count += 2
            energy_used += box * 2
            elf -= box * 2
            elves_energy.append(elf + 1)
        else:
            no_energy = True

    elif elf_num % 5 == 0:
        if elf >= box:
            elf -= box
            energy_used += box
            elves_energy.append(elf)
        else:
            no_energy = True

    elif elf >= box:
        toy_count += 1
        energy_used += box
        elf -= box
        elves_energy.append(elf + 1)

    else:
        no_energy = True

    if no_energy:
        boxes_left.append(box)
        elf *= 2
        elves_energy.append(elf)

print(f'Toys: {toy_count}')
print(f'Energy: {energy_used}')
if elves_energy:
    print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")
if boxes_left:
    print(f"Boxes left: {', '.join(str(x) for x in boxes_left)}")
