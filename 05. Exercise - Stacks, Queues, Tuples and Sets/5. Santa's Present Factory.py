from collections import deque

boxes = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

crafted = {}

presents = {
    150: 'Doll',
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while boxes and magic_level:
    box_power = boxes.pop()
    magic_power = magic_level.popleft()

    if box_power == 0 and magic_power == 0:
        continue

    if box_power == 0:
        magic_level.appendleft(magic_power)
        continue
    if magic_power == 0:
        boxes.append(box_power)
        continue

    total_magic_level = box_power * magic_power
    if total_magic_level in presents:
        toy_name = presents[total_magic_level]
        if toy_name in crafted:
            crafted[toy_name] += 1
            continue
        else:
            crafted[toy_name] = 1
            continue

    if total_magic_level < 0:
        boxes.append(box_power + magic_power)
    else:
        boxes.append(box_power + 15)

if ("Doll" in crafted and "Wooden train" in crafted) or ("Teddy bear" in crafted and "Bicycle" in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join([str(x) for x in reversed(boxes)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")
for key, value in sorted(crafted.items()):
    print(f'{key}: {value}')