from collections import deque

expression = input().split()

nums = deque()

operations = {
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,

}

for x in expression:
    if x in '*/-+':
        while len(nums) > 1:
            left = nums.popleft()
            right = nums.popleft()
            result = operations[x](left,right)
            nums.appendleft(result)
    else:
        nums.append(int(x))

print(nums.pop())