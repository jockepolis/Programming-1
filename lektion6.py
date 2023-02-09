def counter(x, lista):
    res = 0
    for lst in lista:
        if type(lst) == list:
            res += lst.count(x)
        elif lst == x:
            res += 1
    return res