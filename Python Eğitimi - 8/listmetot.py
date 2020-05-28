
#Help() methodu kullanımı
arabalar = ["Mercede","Audi","BMW","Volvo"]

print(help(arabalar))

arabalar = ["Mercede","Audi","BMW","Volvo"]

print(help(arabalar.append))

#LİST METOTLARI
program = ["Python","Java","C","Java Script"]

#Liste'nin eleman sayısını gösterir.
print(len(program)) 

#Alfabede(a-z) ve sayılarda en küçük değeri bulur.
print(min(program)) 

#Alfabede(a-z) ve sayılarda en büyük değeri bulur.
print(max(program)) 

program = ["Python","Java","C","Java Script"]

#Liste sonuna "PHP" ekler
program.append("PHP")
print(program)

#Liste'nin istediğimiz dizine veriyi ekler.
program.insert(1,"Pascal")
print(program)

program = ["Python","Java","C","Java Script"]

#Liste sonundaki veriyi siler.
program.pop()
print(program)

#Liste'nin istediğimiz dizinde yer alan veriyi siler.
program.pop(1)
print(program)

#Liste'den adı girilen dizini siler.
program.remove("C") 
print(program)

program = ["Python","Java","C","Java Script"]

# Listeyi alfabetik sıraya dizer
program.sort()
print(program)

# Listeyi alfabetik sıranın tersine dizer
program.reverse()
print(program)
