from collections import deque

colors = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

secondary_colors_match = {
    "orange": ['red', 'yellow'],
    "purple": ['red', 'blue'],
    "green": ['blue', 'yellow']
}

collected_colors = []
final_colors = []
while colors:
    left = colors.popleft()
    if colors:
        right = colors.pop()
    else:
        right = ''

    result = left + right
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = right + left
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        colors.insert(len(colors) // 2, left)
    if right:
        colors.insert(len(colors) // 2, right)

for color in collected_colors:
    if color in main_colors:
        final_colors.append(color)
        continue
    match = True
    for x in secondary_colors_match[color]:
        if x not in collected_colors:
            match = False
            break
    if match:
        final_colors.append(color)

print(final_colors)

