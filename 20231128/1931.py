n = int(input())

arr = []

for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line) 

count = 0
min = arr[0][0]
which_line = 0

while True:
     if len(arr) <= 1:
          print(count)
          break
    for i in range(n):
        if arr[i][0] < min:
            min = arr[i][0]
            which_line = i
        elif arr[i][0] == min:
            if arr[i][1] < arr[which_line][1]
                min = arr[i][0]
                which_line = i
    count = count+1
    del arr[which_line]


