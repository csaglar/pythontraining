sehir = input("Eviniz hangi şehirde? : ")
alan = float(input("Eviniz kaç metrekare? : "))
bina_yasi = int(input("Evinizin bina yaşı nedir? : "))
fiyat = float(input("Eviniz için ne kadar istiyorsunuz? (TL) : "))

ilan = {
    "sehir" : sehir,
    "alan" : alan,
    "bina_yasi" : bina_yasi,
    "fiyat" : fiyat
}

print("İlanınız",len(ilan),"özellik ile oluşturuldu. Teşekkürler.")
print(ilan.get("sehir"),"ilinde yer alan satılık ev ilanınızın özellikleri:")
print("*",ilan.get("alan"),"metrekare")
print("*",ilan.get("bina_yasi"),"yaşında")
print("*",ilan.get("fiyat"),"TL")


