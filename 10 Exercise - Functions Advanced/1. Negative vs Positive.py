def positive(*args):
    result = 0
    for y in args:
        if y >= 0:
            result += y
    return result


def negative(*args):
    result = 0
    for y in args:
        if y < 0:
            result += y
    return result


data = [int(x) for x in input().split()]

print(negative(*data))
print(positive(*data))

if positive(*data) < abs(negative(*data)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
