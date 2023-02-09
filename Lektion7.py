text = """Kvällens gullmoln fästet kransa.
Älvorna på ängen dansa,
och den bladbekrönta näcken
gigan rör i silverbäcken.
"""

freq = {}               # Skapa ett tomt lexikon
for c in text:          # Iterera över tecknen
    if c.isalpha():        # Vi intresserar oss bara för bokstäver
        c = c.lower()      # Skiljer inte på små och stora
        if c in freq:      # Om denna bokstav redan finns som nyckel
            freq[c] += 1   # Öka dess frekvens
        else:              # annars
            freq[c] = 1    # Lägg in den med frekvensen 1
lista = list(freq.items())
lista.sort()
for index, e in enumerate(lista, start=1):
    print(f'{e[0]}:{e[1]:2d}', end='  ')
    if index % 8 == 0:
        print()
print('\n\n')