#Huiswerk opgave 12 - functie importeren
from algemene_functies import mijn_functie_2

#Huiswerk opgave 5
def aanbieding_1(smaak,prijs,korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 Liter) in de smaak {smaak}, van {prijs}, euro voor {prijs_na_korting} euro."
    return uitvoer
#print(aanbieding_1("aardbei",4,0.1))

#Huiswerk opgave 6
def inkomsten_totaal(inkomsten):
    return sum(inkomsten)
inkomsten =[220,430,125,160,205,90,345]
#print(inkomsten_totaal(inkomsten))

#huiswerk opgave 7
def inkomsten_totaal(inkomsten,btw):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten vn deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden"
    return uitvoer
inkomsten =[220,430,125,160,205,90,345]
btw = 0.09  
#print(inkomsten_totaal(inkomsten,btw))

#huiswerk opgave 8
def laag_en_hoog(mijn_lijst):
    maximum = max(mijn_lijst)
    minimum = min(mijn_lijst)
    uitvoer = (maximum, minimum)
    return uitvoer
mijn_lijst =[220,430,125,160,205,90,345]
#print (laag_en_hoog(mijn_lijst))

#huiswerk opgave 9
def gemiddelde(mijn_lijst):
    return sum(mijn_lijst)/len(mijn_lijst)
    
mijn_lijst =[220,430,125,160,205,90,345]
#print (gemiddelde(mijn_lijst))

#Huiswerk opgave 10
def gemiddelde(mijn_lijst):
    bedrag =  sum(mijn_lijst)/len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer
    
mijn_lijst =[220,430,125,160,205,90,345]
#print (gemiddelde(mijn_lijst))

#Huiswerk opgave 11
def meervoudig(invoer_lijst):
    return list(laag_en_hoog(invoer_lijst))

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
#print (meervoudig (invoer_lijst))

#Huiswerk opgave 12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

invoer_lijst_2 = [12, 5]
resultaat = combinatie(invoer_lijst_2)
print(resultaat)