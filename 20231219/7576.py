from collections import deque
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

Q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1: # 익은
            Q.append((i,j))
        if board[i][j] == 0: # 안익은
            dist[i][j] = -1

while Q:
    cur = Q.popleft()
    for dir in range(4):
        x = cur[0]+dx[dir]
        y = cur[1]+dy[dir]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if board[x][y] != 0 or dist[x][y] != -1:
            continue
        dist[x][y] = dist[cur[0]][cur[1]] + 1
        Q.append((x,y))

ans = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] == -1:
            print(-1)
            break
        ans = max(ans, dist[i][j])

print(ans)