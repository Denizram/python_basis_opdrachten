# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

geheime_getal = random.randint(1, 100)

pogingen = 0

print("Raad mijn geheime getal tussen 1 en 100.")

while True:
    invoer = input("Voer je gok in: ")
    
    try:
        gok = int(invoer)
    except ValueError:
        print("Voer een geldig getal in.")
        continue

    pogingen += 1

    if gok < geheime_getal:
        print("Hoger")
    elif gok > geheime_getal:
        print("Lager")
    else:
        print(f"Je hebt het getal geraden! Het is {geheime_getal}!")
        break

print(f"Je hebt het in {pogingen} keer gedaan.")

