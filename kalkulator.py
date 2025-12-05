def meny():
    print("**Avansert Kalkulator**")
    print("1. Addisjon")
    print("2. Subtraksjon")
    print("3. Multiplikasjon")
    print("4. Divisjon")
    print("5. Potens (x^y)")
    print("6. Kvadratrot")
    print("7. Avslutt")

    valg = input("Velg et tall mellom 1 og 7: ")
    return valg 
# valg returnerer som tekst fordi det er et meny valg og ikke selve tall i kalkulator, husk dette!

def addisjon():
    tall1 = float(input("Skriv inn første tall: "))
    tall2 = float(input("Skriv inn ditt andre tall: "))
    resultat = tall1 + tall2
    print(f"Resultatet av addisjon er: {resultat}")


valg = meny()

if valg == "1":
    addisjon()
