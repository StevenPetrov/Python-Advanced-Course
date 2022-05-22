# clothes = list(map(int, input().split()))
clothes = [int(x) for x in input().split()]

rack_size = int(input())
count = 0
temp_rack = []
while clothes:
    peace = clothes.pop()
    temp_rack.append(peace)
    if sum(temp_rack) == rack_size:
        count += 1
        temp_rack = []
    elif sum(temp_rack) > rack_size:
        clothes.append(peace)
        count += 1
        temp_rack = []
if temp_rack:
    count += 1
print(count)
