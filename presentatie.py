#huiswerk 10 punt 6 - bestand aanmaken
#huiswerk 10 punt 7 - 8
def presenteer(mijn_dict, totaal):
    mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
    totaal = 50

    for key, value in mijn_dict.items():
        print(f"{mijn_dict} : {totaal} euro")

    print("=" * 26)
    print(f"Totaal : {totaal} euro")
    presenteer(mijn_dict,totaal)
