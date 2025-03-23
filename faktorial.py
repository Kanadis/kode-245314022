angka = int(input("Masukkan Angka : "))
faktorial = 1
for i in range (1, angka + 1):
    faktorial *= i
print("Hasil faktorial dari {0} adalah {1}".format(angka,faktorial))