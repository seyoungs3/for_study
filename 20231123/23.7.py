col, row = map(int,input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        try:
            if matrix[i][j]