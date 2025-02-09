#huiswerk 10 punt 1 - bestand aanmaken

#huiswerk 10 punt 4 + 9 + 11
import helper
import presentatie
import csv

#huiswerk 10 punt 2
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

#huiswerk 10 punt 5
totaal_inkomsten = som(inkomsten)
#print(totaal_inkomsten)

#huiswerk 10 punt 10
presenteer = (inkomsten,totaal_inkomsten)
print(presenteer)

#huiswerk 10 punt 12
with open('boekhouding.csv’, 'w',newline='') as csvfile:
      for key, value in inkomsten.items():
      writer = csv.writer(csvfile, delimiter=';')
      writer.writerow([key,value])
