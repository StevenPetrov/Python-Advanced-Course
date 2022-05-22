from collections import deque

green_light = int(input())
free_window = int(input())

q = deque()
car_passed = 0
hit = False
green = green_light
end_program = False
while True:
    if hit: break
    green = green_light
    command = input()
    while command != 'green' and command != 'END':
        q.append(command)
        command = input()
    if command == 'END':
        if not hit:
            print('Everyone is safe.')
            print(f'{car_passed} total cars passed the crossroads.')
    if command == 'green':
        while q:
            car = q.popleft()
            green_light -= len(car)
            if green_light < 0:
                green_light += free_window
                if green_light < 0:
                    print('cheeck')
                else:
                    end_program = True
                    break
            else:
                car_passed += 1
if not hit:
        print('Everyone is safe.')
        print(f'{car_passed} total cars passed the crossroads.')
