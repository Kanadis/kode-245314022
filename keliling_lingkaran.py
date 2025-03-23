import math # untuk bisa menggunakan math.sqrt

titik = [] #list untuk menyimpan kordinat
jumlah_titik = 2
i = 1
while i <= jumlah_titik: #melakukan perulangan sampai i sama dengan jumlah_titik
    titik_x = float(input("Masukkan nilai absis untuk titik {0}   : ".format(i)))
    titik_y = float(input("Masukkan nilai ordinat untuk titik {0} : ".format(i)))
    titik.append((titik_x,titik_y)) 
#append untuk menambahkan isi dari nilai yang telah di masukkan user ke titik
    i+=1 #menambahkan iterasi

(titik_x1,titik_y1) = titik[0] #titik ke-1
(titik_x2,titik_y2) = titik[1] #titik ke-2

jari_jari = math.sqrt((titik_x2-titik_x1)**2 + (titik_y2-titik_y1)**2)

keliling = 2 * math.pi*jari_jari

print(f"Memiliki luas     : {jari_jari:.2f}")
print(f"Memiliki keliling : {keliling:.2f}")
