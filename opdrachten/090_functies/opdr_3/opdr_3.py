# Opdracht 1 functies
# Naam student:
# Groep:

import math

# Functie om het volume van een kubus te berekenen
def kubus_vol(zijde):
    return zijde ** 3  # Volume van een kubus is zijde^3

# Functie om het volume van een bol te berekenen
def bol_vol(radius):
    return (4/3) * math.pi * (radius ** 3)  # Volume van een bol is (4/3) * pi * r^3

# Voorbeeldgebruik:
# Volume van een kubus met zijde 5
volume_kubus = kubus_vol(5)
print(f"De inhoud van deze kubus is: {volume_kubus}")

# Volume van een bol met radius 4
volume_bol = bol_vol(4)
print(f"De inhoud van deze bol is: {volume_bol}")