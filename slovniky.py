
n=int(input("Vlož číslo n: "))

seznam_dvojic = [(i, i**2) for i in range(1,n+1)]
nazvy_cisel = dict(seznam_dvojic)
print(nazvy_cisel)

def soucet(nazvy_cisel):
    """
    Vrací součet kliců a hodnot slovníku.
    """
    soucetKlicu=0
    soucetHodnot=0
    for klic in nazvy_cisel:
        soucetKlicu+=klic

    for hodnota in nazvy_cisel.values():
        soucetHodnot+=hodnota

    return soucetKlicu,soucetHodnot

print(soucet(nazvy_cisel))

retezec=input("Vlož řetězec: ")
def pocetPismenSlovo(retezec):
    seznamPismen=[]
    for i in retezec:
        if i not in seznamPismen:
            seznamPismen.append(i)
    pocetPismen=[]
    for j in seznamPismen:
        pocetPismen.append(retezec.count(j))
    seznam_dvojic = []
    for i,j in zip(seznamPismen,pocetPismen):
            seznam_dvojic.append((i, j))
    slovnikPismen=dict(seznam_dvojic)
    return slovnikPismen

print(pocetPismenSlovo(retezec))

def vypis_slovnik(nazvy_cisel):
    for klic, hodnota in nazvy_cisel.items():
        print('Klíč {}: , hodnota {}'.format(klic, hodnota))
vypis_slovnik(nazvy_cisel)
