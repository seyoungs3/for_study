from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

mx = 0  # 그림의 최댓값
num = 0  # 그림의 수

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or vis[i][j]:
            continue

        num += 1  # 그림의 수 1 증가
        Q = deque()
        vis[i][j] = True  # (i, j)로 BFS를 시작하기 위한 준비
        Q.append((i, j))
        area = 0  # 그림의 넓이

        while Q:
            area += 1  # 큐에 들어있는 원소를 하나 뺄 때 마다 넓이를 1 증가시킴
            cur = Q.popleft()

            for dir in range(4):  # 상하좌우 칸을 살펴볼 것이다.
                nx, ny = cur[0] + dx[dir], cur[1] + dy[dir]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if vis[nx][ny] or board[nx][ny] != 1:
                    continue

                vis[nx][ny] = True  # (nx, ny)를 방문했다고 명시
                Q.append((nx, ny))

        # (i, j)를 시작점으로 하는 BFS가 종료됨
        mx = max(mx, area)  # area가 mx보다 클 경우 mx에 area를 대입.

print(num)
print(mx)
