word = input()
times = input()

try:
    print(word * int(times))
except ValueError:
    print('Variable times must be an integer')
