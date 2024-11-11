# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344

# Functie om miles om te rekenen naar kilometers
def miles_naar_kilometers(miles):
    return miles * 1.609344

# Voorbeeldwaarden
kilometers = 1223
miles = 867

# Omrekeningen uitvoeren
miles_resultaat = kilometers_naar_miles(kilometers)
km_resultaat = miles_naar_kilometers(miles)

# Resultaten afdrukken
print(f"{kilometers} kilometers = {miles_resultaat} miles")
print(f"{miles} miles = {km_resultaat} kilometers")