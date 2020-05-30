araba = ["MERCEDES","VOLVO","BMW","TESLA"]

print("Galerinizde toplam:",len(araba),"araba bulunmaktadır.")
print("MERCEDES,VOLVO,BMW,TESLA")

secim = input("Hangi arabayı almak istiyorsunuz: ") #Araba girişi 
marka = secim.upper() #Girilen araba markasının harflerini büyük yapar.

satis = araba.index(marka) #Girilen araba markasının sırasını gösterir.

print("satılan araba",araba[satis])

araba.remove(marka) #Satılan marka listeden silinir.
araba_sayisi = len(araba) #Liste içindeki verilerin sayısını gösterir.

print("Galeride kalan araba sayısı: ",araba_sayisi)