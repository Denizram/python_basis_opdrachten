# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

def verzamel_antwoorden():
    antwoorden = {}
    
    for i, vraag in enumerate(vragen, start=1):
        antwoord = input(f"{i}. {vraag}\n")
        antwoorden[vraag] = antwoord  
    
    return antwoorden

def schrijf_naar_bestand(antwoorden, bestand):
    with open(bestand, "a", encoding="utf-8") as f:
        f.write("----\n")
        for vraag, antwoord in antwoorden.items():
            f.write(f"{vraag}: {antwoord}\n")
        f.write("\n")  

def main():
    print("Vul de vragenlijst in voor de party.")
    antwoorden = verzamel_antwoorden()
    schrijf_naar_bestand(antwoorden, "feestgangers.txt")
    
    print("\nBedankt voor het invullen!")
    print("See you at the party.")

if __name__ == "__main__":
    main()