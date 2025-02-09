#huiswerk 10 punt 6 - bestand aanmaken
#huiswerk 10 punt 7 - 8
def presenteer(inkomsten, totaal_inkomsten):
    # mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
    # totaal = 50

    for key, value in inkomsten.items():
        print(f"{key} : {value} euro")

    print("=" * 26)
    print(f"Totaal : {totaal_inkomsten} euro")