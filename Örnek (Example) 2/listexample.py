ad = ["Caner","Aren","Çınar"]
soyad = ["Sağlar","Özer","Özer"]
egitim = ["Lisans","Yüksek Lisans","Yüksek Lisans"]

yeni_ad = ad.append("Hakan") #Listeye yeni ad ekler
yeni_soyad = soyad.append("İnan") #Listeye yeni soyad ekler
yeni_egitim = egitim.append("Yüksek Lisans") #Listeye yeni egitim ekler.

personel_sayisi = len(ad) #ad Listesi içindekilerin sayısını verir.
lisans = egitim.count("Lisans") #egitim Listesi'nde ki "Lisans" sayısını verir.
benzer_soyad = soyad.count("Özer") #soyad Listesi'nde ki "Özer" sayısını verir.
index_number = egitim.index("Yüksek Lisans") #"Yüksek Lisans" kaçıncı sırada?

print(ad)
print(soyad)
print(egitim)

print("Toplam",personel_sayisi - lisans,"personelimiz",egitim[index_number], "Mezunudur.")
print("Toplam",benzer_soyad, "personelimizin soyadları aynıdır.")