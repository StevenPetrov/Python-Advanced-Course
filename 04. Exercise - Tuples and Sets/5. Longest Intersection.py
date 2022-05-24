longest_set = list()

lines= int(input())

for x in range(lines):
    temp1, temp2 = input().split('-')
    temp1 = temp1.split(',')
    set1 = set()
    set2 = set()
    for y in range(int(temp1[0]),int(temp1[1])+1):
        set1.add(y)
    temp2 = temp2.split(',')
    for z in range(int(temp2[0]), int(temp2[1]) + 1):
        set2.add(z)
    int_set = set1 & set2
    if len(int_set) > len(longest_set):
        longest_set = int_set

longest_set = list(longest_set)
print(f"Longest intersection is {longest_set} with length {len(longest_set)}")