n = int(input())

matrix = []

for _ in range(n):
    matrix.append([x for x in input()])

symbol = input()


def symbol_check(matrix, symbol):
    for x in matrix:
        for y in x:
            if symbol == y:
                return matrix.index(x), x.index(y)


result = symbol_check(matrix, symbol)

if result:
    row_index, column_index = result
    print(f'({row_index}, {column_index})')
else:
    print(f'{symbol} does not occur in the matrix')
