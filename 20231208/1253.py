import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

count = 0
for k in arr:
    i = 0
    j = n-1
    sum = arr[i] + arr[j]
    while i < j:
        if sum == k:
            if arr[i] != k and arr[i] != k:
                count += 1
                break
            elif arr[i] == k:
                i += 1
            elif arr[j] == k:
                j -= 1
        elif sum < k:
            i += 1
        else:
            j -= 1
        sum = arr[i] + arr[j]

print(count)