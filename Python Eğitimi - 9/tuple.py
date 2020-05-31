#tuple() parantez içerisine alınmadan kullanılabilir.
tuple1 = "Python","Java","C++"
print(type(tuple1))

#tuple() parantez içerisinde kullanılabilir. (ÖNERİLEN)
tuple2 = ("Python","Java","C++")
print(type(tuple2))

#tuple() içerisindeki elemanlar dizin numaraları girilerek çağırılabilir.
tuple = ("Python","Java","C++")
print(tuple[1])

#tuple() başka bir tuple() ile birleştirilebilir.
tuple1 = ("Python","Java","C++")
tuple2 = ("PHP","Pascal","HTML")

new_tuple = tuple1 + tuple2
print(new_tuple)

#tuple() aynı değişken adı üzerine girilen elemanlar diğerinin üzerine yüklenir.
tuple = ("Python","Java","C++")
tuple = (1,"İki",3)

print(tuple)