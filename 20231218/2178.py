from collections import deque

n, m = map(int, input().split())
board = [input() for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Q = deque()
Q.append((0, 0))
dist[0][0] = 0

while Q:
    cur = Q.popleft()

    for dir in range(4):
        nx, ny = cur[0] + dx[dir], cur[1] + dy[dir]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if dist[nx][ny] >= 0 or board[nx][ny] != '1':
            continue

        dist[nx][ny] = dist[cur[0]][cur[1]] + 1
        Q.append((nx, ny))

print(dist[n-1][m-1] + 1)
