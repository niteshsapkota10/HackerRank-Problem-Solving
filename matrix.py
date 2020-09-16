import math
mat = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
d1 = 0
d2 = 0

for i in range(0, len(mat)):
    for j in range(0, len(mat[0])):
        if i == j:
            d1 = d1+mat[i][j]
        if ((i+j) == (len(mat)-1)):
            d2 = d2+mat[i][j]

print(abs(d1-d2))
