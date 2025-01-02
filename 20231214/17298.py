import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))

stack = [0] # 인덱스

answer = [-1 for _ in range(n)]

for i in range(1,n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

for i in answer:
    print(i, end=' ')