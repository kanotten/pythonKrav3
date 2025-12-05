# pythonKrav3
KALKULATOR MED PYTHON

-  [Problemer](#Problemer-oppstått)
-  [Kilder](#kilder-og-verktøy)
-  [Endringer](#endringer) 

## Problemer oppstått

1. Input i menyen

Når bruker skrev inn tekst eller andre tegn enn 1-7, oppstod feil. Dette skyldtes at jeg ikke hadde laget en "while loop" rundt menyen ennå.

2. Ugyldig input i funskjoner

Når man skriver tekst her så får man feil og programmet kræsjer, dette er pågrunn av float og forventer tall. 

3. Divisjon

Siden man ikke kan dele på null, blir bruker sendt helt tilbake til meny istedenfor å bare bli spurt på nytt. her lagde jeg en while loop for å rette opp.

4. Potens

Ved veldig høye tall gir python et overflow porblem og gir derfor ugyldig resultater. dette påvirket ikke oppgaven så det ble ikke endret, men kun observert

5. Kvadratrot

Man kan ikke få kvadratrot av negative tall og gir samme problem med at man blir sendt tilbake til meny. løste dette med nok en "while loop" som i divisjon.

6. Meny loop

Menyens loop ble ganske repeterende med min løsning (if og elif). Jeg fant andre måter å løse dette på, men det var mer avansert enn mitt nivå så hold meg til standard.


## Kilder og verktøy

1. Gokstad Akademiet sitt kursmatriale

spesielt ble linker om conditions, user input og mathematical Operations brukt her. dette dekket det meste av oppgaven.

2. StackOverflow

Her fant jeg en del håndteringer av ugyldig input i en lignende oppgave. de brukte try/except og while. dette ble brukt for forståelse men ikke brukt i min løsning. følte dette var litt over mitt nivå. 

3. ChatGPT

Jeg brukte "Chat" til å få struktur og organisering i hvordan jeg skulle gå frem. noe syntax oppsett i ReadME.
Men ellers er alt hovedsakelig Gokstad sitt matriale. all tekst og kode er skrevet av meg, med egen forståelse.


## Endringer

1. Divisjon

Mtp at første kode i henhold til oppgaven får bruker til å bli sendt tilbake til meny, i den form av at programmer stopper. så endret jeg om til å legge en while loop for bedre UI.

2. Kvadratrot

Om man følger oppgaven til punkt så ville samme tilfelle skje her om man prøver å få rot av negative tall. endret min kode om til å få bedre UI ved en while loop.
