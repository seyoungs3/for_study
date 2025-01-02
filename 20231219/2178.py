from collections import deque
n, m = map(int, input().split())
board = []
for i in range(n):
    line = list(input())
    board.append(line)

vis = [[False for _ in range(m)] for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
Q = deque()
Q.append((0,0))
vis[0][0] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while Q:
    cur = Q.popleft()
    for dir in range(4):
        x = cur[0] + dx[dir]
        y = cur[1] + dy[dir]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if board[x][y] == '0' or vis[x][y]:
            continue
        Q.append((x,y))
        vis[x][y] = True
        dist[x][y] = dist[cur[0]][cur[1]] + 1

print(dist[n-1][m-1]+1)
        
