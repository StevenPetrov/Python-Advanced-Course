def grocery_store(**kwargs):
    store = kwargs
    store = sorted(store.items(), key= lambda key: (-key[1],-len(key[0]), key))
    return '\n'.join([f'{key}: {value}' for key,value in store])

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
