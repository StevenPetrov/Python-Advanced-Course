import re


def read_word():
    with open('./words_lookup') as words:
        return words.read().split()


def count_words(words):
    words_dict = {
        word: 0 for word in words
    }
    with open('./random_text.txt') as text:
        for line in text:
            words_in_line = [w.lower() for w in re.findall(regex, line)]
            for word in words:
                words_dict[word] += words_in_line.count(word.lower())
    return words_dict


regex = '\w+'

words = count_words(read_word())

[print(f'{key} - {value}') for key, value in sorted(words.items(), key=lambda x: -x[1])]
