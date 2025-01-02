col, row = map(int,input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        count = 0
        if matrix[i][j] == '*':
           print('*', end='')
        else:
            try:
                if matrix[i-1][j-1] == '*':
                    count = count+1
                if matrix[i-1][j] == '*':
                    count = count+1
                if matrix[i-1][j+1] == '*':
                    count = count +1
                if matrix[i][j-1] == '*':
                    count = count +1
                if matrix[i][j+1] == '*':
                    count = count +1
                if matrix[i+1][j-1] == '*':
                    count = count +1
                if matrix[i+1][j] == '*':
                    count = count +1
                if matrix[i+1][j+1] == '*':
                    count = count +1
            print(count, end='')

            except:
                continue
           
            
    print()
    