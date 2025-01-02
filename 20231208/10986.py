import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n은 어레이 수, m은 나눌 수

arr = list(map(int, input().split()))

presum = []
temp = 0
for i in range(n):
    temp = temp + arr[i]
    presum.append(temp)

remainder = []
for i in range(n):
    remainder.append(presum[i] % m)

answer = 0
same_r = [0] * m
for i in range(n):
    if remainder[i] == 0:
        answer += 1
    same_r[remainder[i]] += 1

for i in range(m):
    answer = answer + same_r[i] * (same_r[i]-1) // 2

print(answer)