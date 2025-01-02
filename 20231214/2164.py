# 큐
from collections import deque

n = int(input())

A = [i for i in range(1,n+1)]
A = deque(A)

while len(A) != 1:
    A.append(A[1])
    del A[0]
    del A[0]

print(A[0])