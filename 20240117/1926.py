from collections import deque

# 가장 넓은 그림의 넓이 출력

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

vis = [list(0 for _ in range(m)) for _ in range(n)]
Q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and vis[i][j] == 0: # 시작점 설정
            Q.append((i,j))
            vis[i][j] = 1
            while Q:
                cur = Q.popleft()
                for dir in range(4):
                    x, y = cur[0] + dx[dir], cur[1] + dy[dir]
                    if x < 0 or x >= n or y < 0 or y >= m:
                        continue
                    if paper[i][j] == 1 and vis[x][y] == 0:
                        Q.append((x,y))
                        vis[x][y] = 1
                        