from collections import deque
import sys
input = sys.stdin.readline


n = int(input())


A = list(map(int, input().split()))
queue = deque(A)

## 왼쪽에 있는거 제거, 오른쪽에서 자기보다 작으면 제거, 첫번째 인덱스

for i in range(n):
    number = queue.popleft()
    while queue[0] < number:
        queue.popleft()
    print(queue[0], end=' ')