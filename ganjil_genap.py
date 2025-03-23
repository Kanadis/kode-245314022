deretan_angka = [11,12,13,14,15,16,17,18,19,20]
print("Hasil yang diinginkan adalah :")

for x in deretan_angka: 
    if x % 2 == 0: #jika habis dibagi 2 = 0
        print("Angka {0} adalah genap".format(x))
    else: #selain itu
        print("Angka {0} adalah ganjil".format(x))