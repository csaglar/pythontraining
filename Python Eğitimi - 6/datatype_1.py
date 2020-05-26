#İnteger (int)

x = -32
y = 105
z = int("1920")
q = int(87.0)

print(type(x),x)
print(type(y),y)
print(type(z),z)
print(type(q),q)

#Float (float)

x = -32.4
y = 105.7
z = float("1920")
q = float(87)

print(type(x),x)
print(type(y),y)
print(type(z),z)
print(type(q),q)

#Complex (complex)

x = -9+5j
y = 3-7j
z = complex("1920")
q = complex(87)

print(type(x),x)
print(type(y),y)
print(type(z),z)
print(type(q),q)

#String (str)

x = "-32"
y = "105"
z = str(1920)
q = str(87.0)
t = str(6+2j)

print(type(x),x)
print(type(y),y)
print(type(z),z)
print(type(q),q)
print(type(t),t)

# Examples 1

isim = "Ahmet"
yazili1 = int(input("Birinci yazılı notu"))
yazili2 = float(input("İkinci yazılı notu"))
sozlu = int(input("Sözlü notu"))

print(isim,"'in yazılı notları",yazili1,"ve",yazili2)
print(isim,"'in sözlü notu",sozlu)