l = [float(x) for x in input().split()]
checker = dict()

for x in l:
    if x not in checker:
        checker[x] = 0
    checker[x] += 1
    # if x in checker:
    #     checker[x] += 1
    # else:
    #     checker[x] = 1


for key, values in checker.items():
    print(f'{key} - {values} times')