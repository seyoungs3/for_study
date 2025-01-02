from collections import deque

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    farm = [list(0 for _ in range(m)) for _ in range(n)]
    for _ in range(k):
        j,i = map(int, input().split())
        farm[i][j] = 1
    Q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    vis = [list(0 for _ in range(m)) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1 and vis[i][j] == 0:
                Q.append((i,j))
                vis[i][j] = 1
                cnt += 1
            while Q:
                cur = Q.popleft()
                for dir in range(4):
                    x = cur[0] + dx[dir]
                    y = cur[1] + dy[dir]
                    if x < 0 or y < 0 or x >= n or y >= m:
                        continue
                    if vis[x][y] == 1 or farm[x][y] == 0:
                        continue
                    Q.append((x,y))
                    vis[x][y] = 1
    print(cnt)
        