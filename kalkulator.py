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
    tall = float