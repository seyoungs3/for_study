a=[]
for i in range(9):
    line = list(map(int,input().split()))
    a.append(line)

max = a[0][0]
index_i = 0
index_j = 0
for i in range(9):
    for j in range(9):
        if a[i][j]>max:
            max=a[i][j]
            index_i = i
            index_j = j

print(max)
print(index_i+1, index_j+1, sep=' ')