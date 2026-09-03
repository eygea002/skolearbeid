def still_sporsmal(sporsmal, riktig_svar.lower)
    svar =input(sporsmal)
    if svar lower ()==riktig_svar.lower():
        print("riktig")
        return 1
    else print("feil")
        return 0


 #start på quizen
navn = input("hva heter du?")
print("hei",navn +"!")
print("velkommen")
print("du skal få sporsmål")
#poeng starter på 0
poeng=0
#sporsmål 1
poeng=poeng+still_sporsmal(
    hva er hovedstaden i usa?",
"washington d.c"
#sporsmål 2
poeng= poeng+ still_sporsmal(
    "hvor mange elever er i klssen?",
    "15"
)
#sporsmål 3
poeng=poeng + still_sporsmal(hva heter språket vi bruker for ålage denne spårsmålet?",
"python"
)
#sporsmål 4
poeng=poeng+still_sporsmal(
    "hvor mange dager er det i helgen?",
    "2"
)
#sporsmal 5
poeng =poeng +still_sporsmal(
    "hva brukes print()til i python?",
    "vise"
)
"resultat
print()
print ("quizen er ferdig.")
print (navn,"fikk",poeng,"av  5 poeng.")
#tilbakemelding
if poeng==5:
    print("du er en mester!")
    elif poeng>=3:
        print("bra jobbet!")
        else:
            print ("du må øve mer!")
           1. funksjion 
           python
           def still_sporsmal(sporsmal,riktig_svar):
            funksjionen brukes til å stille sporsmål og kontrollere svaret.
            2.parameter
            pyton
            sporsmal
            riktig_svar
            Dette er informasjion som sendes inn til funksjionen.
            3. input
            python
            svar=input(sporsmal)
            Brukeren skriver inn et svar .
            4.if/else
            pyhton 
            if svar.lower()==riktig_svar.lower()
            5.return
            python
            return 1
            hvis svaret er riktig,sender funksjione 1 tilbake
    
            python
            return 0
            hvis svaret er feil,sender funksjionen 0 tilbake
            6.poeng
            python
            poeng=poeng+still_sporsmal(...)
            poengene øker med 1 når svaret er riktig.
            7.Resultat
            python
            print(navn,"fikk",poeng,"av 5 poing.")
            8.if ,elif og else
            python
            if poeng==5:
                print("du er en mester!")
                elif poeng>=3:
                    print("bra jobbet!")
                    else:
                        print("øve mer!")
                        programmet gir forskjellig tilbakemelding basert på poengsummen.
                        hovedkrav
                       / krav          / hvor i koden?
                       /
                       /______________/_____________
                       /Brukerens navn/ input()
                       /Minist 5 spørsmål/5 sporsmål
                       /poeng             /poeng
                       if/elif/else       /resultadelen
                       funksjion          /still_sporsmal()
                       parametere         /sporsmal,
                       riktige svar/
                       /return            /return1 og
                       return 0/
                       /samlet poengsum   /poeng av 5'
                       /teste riktige/gale svar/gjør begge deler i cmd



