word = input()

dd = dict()

for x in word:
    if x not in dd:
        dd[x] = 0
    dd[x] += 1



# for key, value in dd.items():
#     print(f'{key} : {value} time/s')


for key in sorted(dd):
    print(f'{key}: {dd[key]} time/s')