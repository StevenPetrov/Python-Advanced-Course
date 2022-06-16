from os import listdir
from os.path import isdir, join
from io import open


def path_travel(path, files_ext):
    for x in listdir(path):
        if isdir(join(path, x)):
            path_travel(join(path, x), files_ext)
        else:
            ext = x.split('.')[-1]
            if ext not in files_ext:
                files_ext[ext] = []
            files_ext[ext].append(x)


final = {}
path_travel('./', final)

result = dict(sorted(final.items(), key=lambda key: (key[0], key[1])))

with open(f'./report.txt', 'w') as file:
    for key, value in result.items():
        file.write(f'.{key}' + '\n')
        for x in value:
            file.write(f'- - - {x}' + '\n')
