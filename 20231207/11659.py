import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr_sum = [0]
sum = 0
for i in arr:
    sum = sum + i
    arr_sum.append(sum)

for k in range(m):
    i,j = map(int, input().split())
    print(arr_sum[j]-arr_sum[i-1])