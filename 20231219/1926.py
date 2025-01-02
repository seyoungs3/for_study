# 1926

import sys
from collections import deque
input = sys.stdin.readline

n, m  = map(int, input().split())

board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)


vis = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

num = 0
mx = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or vis[i][j] == 1:
            continue
        Q = deque()
        Q.append((i,j))
        vis[i][j] = 1
        num += 1
        area = 0
        while Q:
            cur = Q.popleft()
            area += 1
            for dir in range(4):
                x = cur[0]+ dx[dir]
                y = cur[1]+ dy[dir]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if vis[x][y] == 1 or board[x][y] == 0:
                    continue
                Q.append((x,y))
                vis[x][y] = 1

        mx = max(mx,area)

print(num)
print(mx)