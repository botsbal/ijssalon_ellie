from helper import decoreer

def print_aanbieding():
    
    #dictionary prijzen
    prijzen = {
        "aardbei": 3,
        "vanille": 4,  # Consistent gebruik van kleine letters
        "chocolade": 5,
    }

    #variabele aanbieding
    aanbieding = prijzen["aardbei"] * 0.8
    #print(aanbieding)

    #variabele reclame_tekst
    reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding}"
    reclame_tekst2 = reclame_tekst[:63]

    #print(reclame_tekst)
    #print(reclame_tekst2)

    #tekst in hoofdletters
    reclame_tekst3 = (reclame_tekst2.upper())
    #print(reclame_tekst3)

    #voor drukker
    reclame_tekst4 = reclame_tekst3.split()
    #print(reclame_tekst4)

    #voor flyer
    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el.upper()) #woorden met vijf of meer letters in hoofdletters
        else:
            print(el.lower()) #woorden met 4 of minder karakters in kleine letters

decoreer("Aanbieding")
print_aanbieding()