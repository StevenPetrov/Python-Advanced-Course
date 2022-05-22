from collections import deque

l = input().split(';')
robots = dict()
for x in l:
    y = x.split('-')
    name = y[0]
    time = y[1]
    robots[name] = time

available_robots = [z for z in robots.keys()]
working_robots = {}

def seconds(h,m,s):
    return h*60*60 + m*60 + s

starting_time = [int(x) for x in input().split(':')]
time_to_seconds = seconds(starting_time[0],starting_time[1],starting_time[2])

def read_products():
    result = deque()
    while True:
        line = input()
        if line == 'End':
            break
        result.append(line)
    return result

products = read_products()

while products:
    current_product = products.popleft()
    for x in available_robots:
        pass