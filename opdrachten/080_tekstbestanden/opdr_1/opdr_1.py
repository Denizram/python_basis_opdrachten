# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

antwoorden = []

for vraag in vragen:
    antwoord = input(vraag + "\n")
    antwoorden.append(antwoord)

with open("antwoorden.txt", "w", encoding="utf-8") as bestand:
    for i in range(len(vragen)):
        bestand.write(f"Vraag: {vragen[i]}\nAntwoord: {antwoorden[i]}\n\n")

print("Je antwoorden zijn opgeslagen in 'antwoorden.txt'.")