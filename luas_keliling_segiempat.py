import math # untuk bisa menggunakan math.sqrt

titik = [] #list untuk menyimpan kordinat
jumlah_titik = 4
i = 1
while i <= jumlah_titik: #melakukan perulangan sampai i sama dengan jumlah_titik
    titik_x = float(input("Masukkan nilai absis untuk titik {0}   : ".format(i)))
    titik_y = float(input("Masukkan nilai ordinat untuk titik {0} : ".format(i)))
    titik.append((titik_x,titik_y)) 
#append untuk menambahkan isi dari nilai yang telah di masukkan user ke titik
    i+=1 #menambahkan iterasi

(titik_x1,titik_y1) = titik[0] #titik ke-1
(titik_x2,titik_y2) = titik[1] #titik ke-2
(titik_x3,titik_y3) = titik[2] #titik ke-3
(titik_x4,titik_y4) = titik[3] #titik ke-4

sisi_AB = math.sqrt((titik_x2-titik_x1)**2 + (titik_y2-titik_y1)**2)
sisi_BC = math.sqrt((titik_x3-titik_x2)**2 + (titik_y3-titik_y2)**2)
sisi_CD = math.sqrt((titik_x4-titik_x3)**2 + (titik_y4-titik_y3)**2)
sisi_DA = math.sqrt((titik_x4-titik_x1)**2 + (titik_y4-titik_y1)**2)
#menghitung setiap sisi dari ordinat dan absis

keliling = sisi_AB + sisi_BC + sisi_CD + sisi_DA

#rumus luas menggunakan rumus Shoelace
luas = abs(0.5 * (((titik_x1*titik_y2) + (titik_x2*titik_y3) + (titik_x3*titik_y4) + (titik_x4*titik_y1))
    -((titik_y1*titik_x2) + (titik_y2*titik_x3) + (titik_y3*titik_x4) + (titik_y4*titik_x1))))

print(f"Panjang sisi AB: {sisi_AB:.2f}") #.2f untuk menampilkan 2 angka di belakang " , "
print(f"Panjang sisi BC: {sisi_BC:.2f}")
print(f"Panjang sisi CD: {sisi_CD:.2f}")
print(f"Panjang sisi DA: {sisi_DA:.2f}")
print(f"Memiliki keliling : ",keliling)
print(f"Memiliki luas     : ",luas)