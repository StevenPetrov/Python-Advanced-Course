def naughty_or_nice_list(kids,*args,**kwargs):
    d = {"Nice": [], "Naughty": [], "Not found" : []}
    for kid in args:
        kid = kid.split("-")
        number = int(kid[0])
        count = 0
        name_kid = ''
        for num, role in kids:
            if num == number:
                count += 1
        if count == 1:
            index = -1
            for num, role in kids:
                index += 1
                if num == number:
                    _, name = kids.pop(index)
                    d[kid[1]].append(name)
                    break
    for name_test,role_test in kwargs.items():
        # kid = kid.split("=")
        # name_test = kid[0]
        # role = kid[1]
        count = 0
        for _, name in kids:
            if name_test == name:
                count += 1
        if count == 1:
            index = -1
            for _, name in kids:
                index += 1
                if name_test == name:
                    _, name = kids.pop(index)
                    d[role_test].append(name)
                    break

    for _, name in kids:
        d['Not found'].append(name)

    result = []

    for key, value in d.items():
        if len(value) > 0:
            valllue = ', '.join(value)
            result.append(f'{key}: {valllue}')

    return '\n'.join(result)

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
