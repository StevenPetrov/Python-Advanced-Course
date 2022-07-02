def words_sorting(*args):
    d = dict()
    sum_values =0
    for word in args:
        total = 0
        for x in word:
            total +=ord(x)
        d[word] = total
        sum_values += total
    if sum_values % 2 == 1:
        d = sorted(d.items(), key= lambda key: (-key[1]))
    else:
        d = sorted(d.items(), key=lambda key: (key[0]))
    return '\n'.join([f'{key} - {value}' for key,value in d])

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
