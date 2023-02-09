import matplotlib.pyplot as plt
import csv

# Importera smooth_a och smooth_b från lektion 6
def smooth_a(a, n):
    r = n*[a[0]] + a + n*[a[-1]]
    return [sum(r[i-n:i+n+1]) / len(r[i-n:i+n+1]) for i in range (n, len(r)-n)]

def smooth_b(a,n):
    return [sum(a[i-n-len(a):i+n+1])/ len(a[i-n-len(a):i+n+1]) for i in range(0, len(a))]

# Använd koden från 8A för att skapa lexikonet
with open('/Users/jockepolis/Desktop/UPPSALA/År 3/PROGG I/CO2Emissions_filtered.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    dict_from_csv = {rows[1]:rows[3:] for rows in reader}
    del dict_from_csv['Country Code']
    new_dict = dict((k.lower(), [float(s) for s in v]) for k, v in dict_from_csv.items())

    # Skapa ett nytt lexikon med endast de nordiska ländernas data
    keys = ['dnk', 'fin', 'isl', 'nor', 'swe'] # Nycklarna som söks
    nordic_dict = {x:new_dict[x] for x in keys} # Dict comprehension för de nordiska länderna

# Skapa tidsvektorn (x-axeln) som vi kommer plotta samtliga värden mot
time = list(range(1960, 2015))

# Skapa figuren där alla plottar kommer befinna sig i samma figur
fig, ax = plt.subplots()
ax.set(xlabel='Year', ylabel='CO2 Emissions (kt)', title='Yearly Emissions of C02 in the Nordic Countries') # Rubriker o.s.v.

# Plotta mätvärdena för CO2-utsläppen för de olika länderna rakt av som cirklar
plt.plot(time, nordic_dict['dnk'],'b:' ,label='Denmark')
plt.plot(time, nordic_dict['fin'], 'y:' ,label='Finland')
plt.plot(time, nordic_dict['isl'], 'm:' ,label='Iceland')
plt.plot(time, nordic_dict['nor'], 'r:' ,label='Norway')
plt.plot(time, nordic_dict['swe'], 'g:' ,label='Sweden')
plt.legend() # Se till att 'legend'rutan finns


n = 5 # Fem ytterligare datapunkter kring ett mittår

# Skapa ett nytt lexikon där funktionen smooth_a går igenom samtliga listor i nordic_dict (ta bort brus)
nordic_dict_smooth_a = dict((k, smooth_a(v,n)) for k, v in nordic_dict.items())

# Plotta värdena ur det nya lexikonet som linjer fast i samma färger som motsvarande land sedan tidigare
plt.plot(time, nordic_dict_smooth_a['dnk'],'b')
plt.plot(time, nordic_dict_smooth_a['fin'], 'y')
plt.plot(time, nordic_dict_smooth_a['isl'], 'm')
plt.plot(time, nordic_dict_smooth_a['nor'], 'r')
plt.plot(time, nordic_dict_smooth_a['swe'], 'g')

# Skapa ett nytt lexikon där funktionen smooth_b går genom samtliga listor i nordic_dict (ta bort brus)
nordic_dict_smooth_b = dict((k, smooth_b(v,n)) for k, v in nordic_dict.items())

# Plotta värdena ur det nya lexikonet som streck fast i samma färger som motsvarande land sedan tidigare
plt.plot(time, nordic_dict_smooth_b['dnk'],'b--')
plt.plot(time, nordic_dict_smooth_b['fin'], 'y--')
plt.plot(time, nordic_dict_smooth_b['isl'], 'm--')
plt.plot(time, nordic_dict_smooth_b['nor'], 'r--')
plt.plot(time, nordic_dict_smooth_b['swe'], 'g--')
plt.show() # Visa figuren




    

