def age_assignment(*args, **kwargs):
    final = dict()
    for name in args:
        final[name] = kwargs[name[0]]
    sorted(final)
    return '\n'.join([f"{name} is {age} years old." for name, age in sorted(final.items())])


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
