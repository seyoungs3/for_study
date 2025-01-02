n = int(input())

arr = []

for i in range(n):
     line = list(map(int, input().split()))
     arr.append(line)

count = 0

fastest = arr[0][1]
which_line = 0
count_False = 0

while True:

    if count_False == len(arr):
        print(count)
        break


    for i in range(len(arr)):
        if arr[i][1] <= fastest and len(arr[i]) == 2:
            if arr[i][1] <= arr[which_line][1]:
                fastest = arr[i][1]
                which_line = i
    # fastest 결정
    print('fastest:', fastest)
    count = count + 1
    print('count_False:', count_False)

    for i in range(len(arr)):
        if arr[i][0] < fastest and len(arr[i]) == 2:
            arr[i].append('False')
            count_False = count_False + 1
        




