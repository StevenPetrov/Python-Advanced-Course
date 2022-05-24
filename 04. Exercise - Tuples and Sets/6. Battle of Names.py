even = set()
odd = set()

for x in range(1,int(input())+1):
    name = input()
    sum_value_name = 0
    for y in name:
        sum_value_name += ord(y)
    sum_value_name /= x
    if int(sum_value_name) % 2 == 0:
        even.add(int(sum_value_name))
    else:
        odd.add(int(sum_value_name))

if sum(odd) == sum(even):
    result = odd.union(even)
elif sum(odd) > sum(even):
    result = odd.difference(even)
elif sum(odd) < sum(even):
    result = odd.symmetric_difference(even)

print(*result, sep =', ')
