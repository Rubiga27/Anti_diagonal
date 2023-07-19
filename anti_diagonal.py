n = int(input("Enter the size of the square matrix: "))

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


anti_diagonals = []
for i in range(n):
    diagonal = []
    for j in range(i, -1, -1):
        diagonal.append(matrix[j][i - j])
    anti_diagonals.append(diagonal)

for i in range(1, n):
    diagonal = []
    for j in range(n - 1, i - 1, -1):
        diagonal.append(matrix[j][n - j + i - 1])
    anti_diagonals.append(diagonal)


for diagonal in anti_diagonals:
    print(' '.join(map(str, diagonal)))
