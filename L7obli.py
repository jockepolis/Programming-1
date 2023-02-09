import re

# Ansätt de n vanligaste orden och de m ovanligaste orden
n = int(input('Insätt antalet vanliga ord n: '))
m = int(input('Insätt antalet ovanliga ord m: '))

# Läs in filen och läs den
dikt = open('/Users/jockepolis/Desktop/UPPSALA/År 3/PROGG I/boye.txt', 'r')

# Omvandla filens innehåll till en sträng med endast små bokstäver
text = ''
for i in dikt:
    i = i.lower()
    text += i
dikt.close() # Stäng alltid filen

# Skapa en ordlista m.h.a. re.findall från lektion 7
wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ0-9]+', text)
print('Antalet ord i dikten: ', len(wordlist)) # Längden av ordlistan motsvarar antalet ord i dikten

# Skapa ett lexikon där frekvensen för vardera ord beräknas
freq = {}              # Skapa ett tomt lexikon
for c in wordlist:     # Iterera över ordlistan
    if c in freq:      # Om detta ord redan finns som nyckel
        freq[c] += 1   # Öka dess frekvens
    else:              # annars
        freq[c] = 1    # Lägg in den med frekvensen 1

# Omvandla lexikonet till en lista
lista = list(freq.items())
print('Antalet olika ord i dikten: ', len(lista)) # Längden av denna lista motsvarar antalet olika ord i dikten

# Använder funktionen från lektionen för att skapa en frekvenssorterad lista från högst frekvens till lägst av samtliga tupler 
# Funktionen part 2 skapas p.g.a. listelementen består av tupler
def part2(e):
    return e[1]
freq_order = sorted(lista, key=part2, reverse=True)

# "Dubbla" for-loops för att kunna indexera i listan av tupler för att sedan använda sig av isinstance-funktionen på tuplarna
# och returnera strängdelen av dem i en lista(fortfarande sorterat från högst till lägst m.a.p. frekvensen)
u = [item for t in freq_order for item in t if isinstance(item,str) is True]

# Skriver ut de n och m vanligaste och ovanligaste orden i dikten
print('De ' + str(n) + ' vanligaste orden i dikten är: ')
print(', '.join(u[:n])) # Join tar alla föremål i en iterabel (lista,tupler) och gör det till en sträng

print('De ' + str(m) + ' ovanligaste orden i dikten är: ')
u.reverse() # Vänder på listan för att den ska gå från lägst frekvens till högst
print(', '.join(u[:m]))