# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

try:
    eerste = int(input("Geef lengte eerste zijde aan \n"))
    tweede = int(input("Geef lengte tweede zijde aan \n"))

    derde = eerste**2 + tweede**2
    antwoord = math.sqrt(derde)

    print (antwoord)
except ValueError:
   print("Hey, dat is geen getal!")