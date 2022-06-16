from io import open

file = open('./text.txt', 'w')
file.write('''-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
''')
file.close()

symbols = {"-", ",", ".", "!", "?"}

with open('./text.txt', 'r') as file:
    for count, line in enumerate(file):
        if count % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for symbol in symbols:
                result = result.replace(symbol, '@')

            print(result)
