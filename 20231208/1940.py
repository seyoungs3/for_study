import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = list(map(int, input().split()))

arr.sort()

i = 0
j = n-1
sum = arr[i]+arr[j]
count = 0

while i < j:
    if sum == m:
        count += 1
        i += 1
        j -= 1
    elif sum < m:
        i += 1
    else:
        j -= 1
    sum = arr[i] + arr[j]

print(count)