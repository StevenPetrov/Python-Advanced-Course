def concatenate(*args,**kwargs):
    l = ''.join(args)

    for key, value in kwargs.items():
        l = l.replace(key,value)
    return l


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))