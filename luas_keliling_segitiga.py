import math # untuk bisa menggunakan math.sqrt

titik = [] #list untuk menyimpan kordinat
jumlah_titik = 3
i = 1
while i <= jumlah_titik: #melakukan perulangan sampai i sama dengan jumlah_titik
    titik_x = float(input("Masukkan nilai absis untuk titik {0}   : ".format(i)))
    titik_y = float(input("Masukkan nilai ordinat untuk titik {0} : ".format(i)))
    titik.append((titik_x,titik_y)) 
#append untuk menambahkan isi dari nilai yang telah di masukkan user ke titik
    i+=1 #menambahkan iterasi

(titik_x1,titik_y1) = titik[0] #titik pertama
(titik_x2,titik_y2) = titik[1] #titik kedua
(titik_x3,titik_y3) = titik[2] #titik ketiga

sisi_a = math.sqrt((titik_x2 - titik_x1)**2 + (titik_y2 - titik_y1)**2)
sisi_b = math.sqrt((titik_x3 - titik_x2)**2 + (titik_y3 - titik_y2)**2)
sisi_c = math.sqrt((titik_x3 - titik_x1)**2 + (titik_y3 - titik_y1)**2)
#math.sqrt untuk mengitung akar

keliling = sisi_a + sisi_b + sisi_c

s = keliling/2
luas = math.sqrt(s * (s - sisi_a) * (s - sisi_b) * (s - sisi_c))

print(f"Panjang sisi a: {sisi_a:.2f}") #.2f untuk menampilkan 2 angka di belakang " , "
print(f"Panjang sisi b: {sisi_b:.2f}")
print(f"Panjang sisi c: {sisi_c:.2f}")
print(f"Memiliki keliling : ",keliling)
print(f"Memiliki luas     : ",luas)
