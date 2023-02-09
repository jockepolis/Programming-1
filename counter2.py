def counter2(x, lista):
    res = 0
    for lst in lista:
        res += lst.count(x)
    return res