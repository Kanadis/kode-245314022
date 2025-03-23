angka = float(input("Masukkan bilangan positif di bawah 20 : "))
while angka <= 0 or angka >= 20:
    print("Angka harus lebih dari 0 dan kurang dari 20! Coba lagi.")
    angka = float(input("Masukkan bilangan positif di bawah 20: "))
x = 20

#perulangan menggunakan while
while angka < x :
    print(x)
    x -= 1
    if angka == x: #berhenti ketika angka = x
        break

#perulangan menggunakan for
for angka in range (x) : 
    print(x)
    x -= 1
    if angka == x: #berhenti ketika angka = x
        break