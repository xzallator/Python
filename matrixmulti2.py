# matriks A
matrix_a = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

# matriks B
matrix_b = [[10, 11, 12],
            [13, 14, 15],
            [16, 17, 18]]

# matriks size
m = len(matrix_a)
n = len(matrix_b[0])
p = len(matrix_b)

# Matriks hasil perkalian
result = [[0 for _ in range(n)] for _ in range(m)]

# Perkalian matriks
for i in range(m):
    for j in range(n):
        for k in range(p):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

# hasil perkalian
for row in result:
    print(row)