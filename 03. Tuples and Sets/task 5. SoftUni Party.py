reservation_list = set()

for _ in range(int(input())):
    reservation_list.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    if guest in reservation_list:
        reservation_list.remove(guest)

not_came = [x for x in reservation_list]

not_came.sort()

print(len(not_came))
[print(x) for x in not_came]