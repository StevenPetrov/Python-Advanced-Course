from io import open
from string import punctuation


def alpha_punc_checker(line):
    letters = 0
    punc = 0
    for sign in line:
        if sign == ' ':
            continue
        elif sign.isalpha():
            letters += 1
        elif sign in punctuation:
            punc += 1
    return letters, punc


file = open('./text2.txt', 'w')
file.write('''-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
''')
file.close()

with open('./text2-output.txt', 'w') as test:
    pass

with open('./text2.txt') as file:
    for count, line in enumerate(file):
        letters_count, punc_count = alpha_punc_checker(line)
        with open('./text2-output.txt', 'a') as test:
            test.write(f'Line {count + 1}: {line.strip()} ({letters_count})({punc_count})\n')
