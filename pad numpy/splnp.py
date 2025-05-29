import numpy as np
#koefisien dari persamaan 1 dan 2
koefisien = ([[2, 3], #persamaan 1
            [3, 4]])  #persamaan 2
#konstanta dari persamaan 1 dan 2
konstanta = ([8, 11])

hasil = np.linalg.solve(koefisien, konstanta)

print("X = ", hasil[0])
print("Y = ", hasil[1])