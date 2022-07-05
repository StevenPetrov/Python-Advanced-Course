def shopping_cart(*args):
    d = {'Soup': [], 'Pizza': [], 'Dessert': []}

    for items in args:
        if items == 'Stop':
            break
        type, item = items
        if type == 'Soup' and len(d[type]) < 3 and item not in d[type]:
            d[type].append(item)
        elif type == 'Pizza' and len(d[type]) < 4 and item not in d[type]:
            d[type].append(item)
        elif type == 'Dessert' and len(d[type]) < 2 and item not in d[type]:
            d[type].append(item)

    count = 0
    for key,value in d.items():
        if len(value) > 0:
            count += 1
    if count == 0:
        return f'No products in the cart!'


    result = []

    for key, value in d.items():
        d[key] = sorted(value)
    d = dict(sorted(d.items(), key=lambda key: (-len(key[1]),key)))

    for key, value in d.items():
        key = key + ':'
        result.append(key)
        for x in value:
            demo = ' - ' + x
            result.append(demo)

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
