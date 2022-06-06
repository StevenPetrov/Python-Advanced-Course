def even_odd(*args):
    operator = args[-1]
    l = []
    if operator == 'even':
        for x in args:
            if isinstance(x,int) and x % 2 == 0:
                l.append(x)
    elif operator == 'odd':
        for x in args:
            if isinstance(x,int) and x % 2 != 0:
                l.append(x)
    return l
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))