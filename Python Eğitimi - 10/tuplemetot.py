
mevsimler = ("İlkbahar","Yaz","Sonbahar","Kış")

print(help(mevsimler))
print(help(mevsimler.count))

#Listede yer alan elemandan kaç adet olduğunu gösterir.
print(mevsimler.count("İlkbahar"))

#Listede yer alan elemanın kaçıncı dizinde yer aldığını gösterir.
print(mevsimler.index("Sonbahar"))

#index() aramasının hangi dizinden başlayacağını belirtir.
print(mevsimler.index("Yaz",1))

#index() aramasının hangi dizinden başlayıp biteceğini belirtir.
print(mevsimler.index("İlkbahar",1,3))