import random

seznamOtazek=["Kdo?","S kým?","Co dělali?","Kde?", "Kdy?","Proč?"]
seznamDvojic=[]
print("Ahoj, vítej v mé hře. Postupně se tě bude ptát na soubor otázek. Pokud nechceš zadávat další odpoveď na danou otázku, zmáčkni enter.")
for otazka in seznamOtazek:
    odpovedi=[]
    odpoved=0
    while odpoved!="":
        odpoved=input(otazka)
        odpovedi.append(odpoved)
    vybranaOdpoved=random.choice(odpovedi)
    seznamDvojic.append((otazka,vybranaOdpoved))
slovnikDvojic=dict(seznamDvojic)
veta=[]
for hodnota in slovnikDvojic.values():
    veta.append(hodnota)
veta=" ".join(veta)
print(veta)
