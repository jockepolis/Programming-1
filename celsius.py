import math

def triangle_area(a, b, c):
    s = (a + b + c)/2
    t = s*(s-a)*(s-b)*(s-c)
    if a <= 0 or b <= 0 or c <= 0 or t <= 0:
        raise ValueError('Illegal parameter values in triangle_area')
    r = math.sqrt(t)
    return r



