# 뿌요뿌요
# 몇연쇄가 되는지 출력

# .은 빈공간
# R G B P Y
# 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 없어짐
# 입력은 뿌요들이 전부 아래로 떨어진 뒤의 상태

# 12개의 줄
# 각 줄에는 6개의 문자

# 4개 이상 연결 되어있는지 판단
# 아래로 내리는 함수 -> board 변경이 일어남

# 여러 그룹이 터지더라도 한번의 연쇄로 계산

# flood fill -> BFS
# 넓이가 4보다 크면 터짐

# 엉엉 테스트케이스는 되는데 틀렸다고 뜸ㅠㅠ

from collections import deque

def bfs(board):
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                Q.append((i,j))
                vis[i][j] = 1
                points = [[i,j]]
                area = 1
                while Q:
                    cur = Q.popleft()        
                    for dir in range(4):
                        x = cur[0] + dx[dir]
                        y = cur[1] + dy[dir]
                        if x < 0 or x >= 12 or y < 0 or y >= 5:
                            continue
                        if board[x][y] == '.' or vis[x][y] == 1:
                            continue
                        if board[cur[0]][cur[1]] == board[x][y]: # 같은 문자일 경우에만 큐에 추가
                            Q.append((x,y))
                            vis[x][y] = 1
                            area += 1
                            points.append([x,y])
                if area >= 4:
                    delneeded.append(points)
                points = []

def movingpoints():
    for block in delneeded:
        for x, y in block:
            board[x][y] = 1
    for j in range(6):
        temp = []
        for i in range(11,-1,-1):
            if board[i][j] == 1:
                continue
            else:
                temp.append(board[i][j])
        while len(temp) != 12:
            temp.append('.')
        idx = 0
        for i in range(11,-1,-1):
            board[i][j] = temp[idx]
            idx += 1

board = [list(input()) for _ in range(12)]
excnt = 0
delneeded = []

Q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
vis = [[0 for _ in range(6)] for _ in range(12)]

bfs(board)

while delneeded:
    movingpoints()
    delneeded = []
    excnt+=1
    vis = [[0,0,0,0,0,0] for _ in range(12)]
    bfs(board)

print(excnt)