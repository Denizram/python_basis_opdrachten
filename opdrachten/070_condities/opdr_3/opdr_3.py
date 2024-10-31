# Opdracht 3 condities
# Naam student:
# Groep:


normale_toegangsprijs = 12.50
kortings_percentages = { "baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30 }
leeftijd = { "baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150) }

bezoeker_leeftijd = int(input("Voer uw leeftijd in: "))

prijs = normale_toegangsprijs

for categorie, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= bezoeker_leeftijd <= max_leeftijd:
        korting = kortings_percentages[categorie]
        prijs -= (prijs * korting / 100)
        break

print(f"De toegangsprijs voor een {categorie} is: €{prijs:.2f}")