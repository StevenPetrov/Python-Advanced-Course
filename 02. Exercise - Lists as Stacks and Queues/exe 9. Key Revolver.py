from collections import deque

bullet_price = int(input())
size_gun_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
values = int(input())

bullet_used = 0
barrel_count = size_gun_barrel

out_of_ammo = False
while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        out_of_ammo = True
        break
    bullet = bullets.pop()
    lock = locks.popleft()
    if bullet <= lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(lock)
    bullet_used += 1
    barrel_count -= 1
    if barrel_count == 0 and bullets:
        print('Reloading!')
        barrel_count = size_gun_barrel

money = values - bullet_price * bullet_used


if not out_of_ammo:
    print(f'{len(bullets)} bullets left. Earned ${money}')