import random

evsahibi = input ("Evsahibi Takım Adı : ")
deplasman = input ("Deplasman Takım Adı : ")

evsahibi_gol = random.randint(0,5)
deplasman_gol = random.randint(0,5)

if evsahibi_gol > deplasman_gol:
    print(evsahibi, "maçı", evsahibi_gol, "-", deplasman_gol, "kazandı.")
elif evsahibi_gol < deplasman_gol:
    print(deplasman, "maçı", deplasman_gol, "-", evsahibi_gol, "kazandı.")
else:
    print("Maç", evsahibi_gol , "-", deplasman_gol, "berabere tamamlandı")