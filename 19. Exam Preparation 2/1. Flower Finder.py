from collections import deque

vowels = deque(input().split())
consonants = input().split()
words = {"rose": [], "tulip": [], "lotus": [], "afodil": []}
found_words = False
while vowels and consonants and not found_words:
    vow = vowels.popleft()
    con = consonants.pop()
    for key in words:
        if vow in key:
            words[key].append(vow)
        if con in key:
            words[key].append(con)
    for keys in words:
        if len(keys) == len(words[keys]):
            temp = words[keys]
            for letter in keys:
                if letter in temp:
                    temp.remove(letter)
            if len(temp) == 0:
                found_words = True
                word = keys
                break

if found_words:
    print(f'Word found: {word}')
else:
    print(f'Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')