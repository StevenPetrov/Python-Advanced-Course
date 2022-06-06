def even_odd_filter(**kwargs):
    result = dict()
    for key, value in kwargs.items():
        if key == 'even':
            result["even"] = []
            for x in value:
                if x % 2 == 0:
                    result["even"].append(x)
        elif key == 'odd':
            result["odd"] = []
            for x in value:
                if x % 2 != 0:
                    result["odd"].append(x)
    result = dict(sorted(result.items(), key= lambda item: -len(item[1])))
    return result



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
