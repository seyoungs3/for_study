arr = []

for i in range(9):
    line = []
    for j in range(9):
        line.append(0)
    arr.append(line)
    
for i in range(9):
        arr[i] = int(input())
        
print(max(arr))
print(arr.index(max(arr)))
