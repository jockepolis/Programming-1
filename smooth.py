# Ta emot en lista a med tal och ett positivt heltal n
def smooth_a(a, n):
    r = n*[a[0]] + a + n*[a[-1]] # Gör en ny lista r som är likt a fast förlängs med n element innan och efter av a[0] och a[-1]
    return [sum(r[i-n:i+n+1]) / len(r[i-n:i+n+1]) for i in range (n, len(r)-n)]
# List comprehension, returnerar summan av listan enligt uppgift genom längden av den för n till längden av r minus n


# Smooth_b, ta emot en lista a med tal och ett positivt heltal n
def smooth_b(a,n):
    return [sum(a[i-n-len(a):i+n+1])/ len(a[i-n-len(a):i+n+1]) for i in range(0, len(a))]
# List comprehension, är detsamma som för smooth_a bara att ingen ny lista r behöver skapas då man ej förlänger listan utan
# istället utnyttjar man att t.ex a[-9]=a[0] eller a[9]=a[8] (utanför listan a)


# Avrunda a_list till ndigits decimaler
def round_list(a_list, ndigits):
    res = [] # Skapar en tom lista
    for i in a_list:
        res.append(round(i, ndigits)) # Fyller på listan med det i:te elementet i den anropade listan och avrundar till ndigits decimaler
    return res


x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1)) 
print('smooth_a(x, 2): ', smooth_a(x, 2))
print('smooth_b(x, 1): ', smooth_b(x, 1))
print('smooth_b(x, 2): ', smooth_b(x, 2))
print('smooth_a(x, 1) rounded: ', round_list(smooth_a(x, 1), 2))

