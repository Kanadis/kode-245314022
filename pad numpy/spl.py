koefisien_x1, koefisien_y1, konstanta_1 = 2, 3, 8
koefisien_x2, koefisien_y2, konstanta_2 = 3, 4, 11

#menyamakan nilai x yang ingin di eliminasi
koefisien_x1 *= 3
koefisien_y1 *= 3
konstanta_1 *= 3

koefisien_x2 *= 2
koefisien_y2 *= 2
konstanta_2 *= 2
#mengeliminasi x dengan mengurangi baris 1 dengan baris 2
koefisien_x = koefisien_x1 - koefisien_x2 
koefisien_y = koefisien_y1 - koefisien_y2
konstanta = konstanta_1 - konstanta_2

koefisien_Y = konstanta / koefisien_y
#memasukkan nilai Y ke persamaan pertama
koefisien_X = (8 - 3*koefisien_Y)/2

print("X = {0} dan Y = {1}".format(koefisien_X, koefisien_Y))
