angka = float(input("Masukkan angka : "))
hasil  = 0
counter = 1
while counter <= angka:  # Loop selama counter masih kecil dari sama dengan angka
    hasil += counter  # Tambahkan counter ke hasil
    counter += 1  # Naikkan counter
print("Jumlah ",hasil)