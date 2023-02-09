import csv

# En funktion där filnamnet är input och ett lexikon är output
def load_csv(filename):
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        dict_from_csv = {rows[1]:rows[3:] for rows in reader} # Skapa ett lexikon utan landsnamnen samt indikatornamnen
        del dict_from_csv['Country Code'] # Ta bort hela den första raden
        # Nytt lexikon skapas med endast små bokstäver och där talen är flyttal och inte strängar, dict comprehension
        new_dict = dict((k.lower(), [float(s) for s in v]) for k, v in dict_from_csv.items()) 
    return(new_dict)

print(load_csv('/Users/jockepolis/Desktop/UPPSALA/År 3/PROGG I/CO2Emissions_filtered.csv'))