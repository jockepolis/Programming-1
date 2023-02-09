import random

def random_shuffle(lst):
    res = []
    for i in lst:
        res.append(lst[random.randint(0,len(lst)-1)])
    return res

print(random_shuffle([1, 2, 3, 4, 5]))