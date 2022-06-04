def operate(operator, *args):
    def add(*args):
        result = 0
        for x in args: result += x
        return result

    def subtract(x,*args):
        result = x
        for y in args: result += -y
        return result

    def multiply(*args):
        result = 1
        for x in args: result *= x
        return result

    def divide(x,*args):
        result = x
        for y in args: result /= y
        return result

    if operator == '+':
        return add(*args)
    if operator == '-':
        return subtract(*args)
    if operator == '*':
        return multiply(*args)
    if operator == '/':
        return divide(*args)


print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))

print(operate("/", 3, 4,2,3))