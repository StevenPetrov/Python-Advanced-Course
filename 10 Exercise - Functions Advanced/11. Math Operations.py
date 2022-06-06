from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    result = dict(kwargs)
    for x in range(1, len(nums) + 1):
        temp_number = nums.popleft()
        if x % 4 == 1:
            result['a'] += temp_number
        elif x % 4 == 2:
            result['s'] -= temp_number
        elif x % 4 == 3:
            if result['d'] == 0 or temp_number == 0:
                continue
            result['d'] /= temp_number
        else:
            result['m'] *= temp_number

    result = dict(sorted(result.items(), key=lambda key: (-key[1], key[0])))
    return '\n'.join([f'{key}: {value:.1f}' for key, value in result.items()])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
