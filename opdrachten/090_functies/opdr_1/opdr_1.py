# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(filename, text):
    # Open het bestand in 'append' modus (a) zodat tekst wordt toegevoegd
    with open(filename, 'a') as file:
        file.write(text + '\n')  # Voeg een nieuwe regel toe na de tekst

# Voorbeeldgebruik van de functie
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"

write_to_file(my_file, my_tekst)
