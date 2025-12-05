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

def subtraksjon():
    tall1 = float(input("Skriv inn første tall: "))
    tall2 = float(input("Skriv inn ditt andre tall: "))
    resultat = tall1 - tall2
    print(f"Resultatet av subtraksjon er: {resultat}")

def multiplikasjon():
    tall1 = float(input("Skriv inn første tall: "))
    tall2 = float(input("Skriv inn ditt andre tall: "))
    resultat = tall1 * tall2
    print(f"Resultat av multiplikasjon er: {resultat}")

def divisjon():
    tall1 = float(input("Skriv inn første tall: "))
   
    while True:
        tall2 = float(input("Skriv inn ditt andre tall: "))
        if tall2 != 0:
            break
        print("Feil!: Kan ikke dele på 0. Prøv igjen :) ")

    resultat = tall1 / tall2
    print(f"Resultatet av divisjon er: {resultat}")
    #Her oppstod det først problem med at brukeren bare ville blitt sendt tilbake til hovedmeny, syns dette var dårlig å prøvde en bedre løsning.
    
def potens():
    grunnverdi = float(input("Skriv inn grunnverdi (x): "))
    eksponent = float(input("Skriv inn eksponten (y): "))
    resultat = grunnverdi ** eksponent
    print(f"Resultatet av {grunnverdi} opphøyd i {eksponent} er: {resultat}")
#Her kan det oppstå feil ved for høye tall, eller string som i tekst. jeg legger til en løsning jeg fant ut: 

def kvadratrot():
    while True:
        tall = float(input("Skriv inn et tall: "))
        if tall >= 0:
            break
        print("Feil!: Kan ikke ta kvadratrot av negative tall. prøv igjen :) ")
    
    resultat = tall ** 0.5
    print(f"Kvadratroten av {tall} er: {resultat}")




    

while True:
    valg = meny()

    if valg == "1":
        addisjon()

    elif valg == "2":
        subtraksjon()

    elif valg == "3":
        multiplikasjon()

    elif valg == "4":
        divisjon()

    elif valg == "5":
        potens()
   

    elif valg == "6":
        kvadratrot()

    elif valg == "7":
        print("avslutter kalkulator, takk for at du prøvde mitt programm! ")
        break

    else:
        print("Hmmm, sikker på at du trakk et tall mellom 1-7? Prøv igjen :)")



    


