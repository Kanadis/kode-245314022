matrik_1 = [[1, 3],
            [4, 6]]
matrik_2 = [[4, 2],
            [6, 1]]

hasil = [[0, 0],
        [0, 0]]

for i in range(2): #mengarah pada matrik 1
    for j in range(2): #mengarah pada matrik 2
        hasil[i][j] = matrik_1[i][j] * matrik_2[i][j]
for jumlah in hasil: # agar tersusun menjadi matrik pada saat di cetak
    print(jumlah)