# 직접 짠 거 아님
# 다시 공부하기 바람
# 특히 진수로 접근하는 방법

n = int(input())
board1 = [list(map(int, input().split())) for _ in range(n)]
board2 = [[0] * n for _ in range(n)]

def rotate(): # 시계 방향으로 90도 돌리는 함수
    global board2
    tmp = [row[:] for row in board2]
    for i in range(n):
        for j in range(n):
            board2[i][j] = tmp[n - 1 - j][i]

def tilt(dir):
    global board2
    for _ in range(dir): # dir 횟수만큼 회전
        rotate()
    for i in range(n): # 각 행마다 진행
        tilted = [0] * n
        idx = 0
        for j in range(n): # 왼쪽으로 기울일 거임
            if board2[i][j] == 0: # 0이면 안넣음
                continue
            if tilted[idx] == 0: # 비어있으면 추가
                tilted[idx] = board2[i][j] 
            elif tilted[idx] == board2[i][j]: # 같으면 값 2배
                tilted[idx] *= 2
                idx += 1 # 다음칸으로 넘어감
            else: # 안비어있는데 값이 다르면 다음칸에 저장
                idx += 1
                tilted[idx] = board2[i][j]
        board2[i] = tilted[:] # 완성값을 board2에 복사함

mx = 0
for tmp in range(1024):
    for i in range(n):
        board2[i] = board1[i][:]
    brute = tmp
    for _ in range(5): # 5개 값 나옴
        dir = brute % 4 # 나머지
        brute //= 4 # 몫 -> 이걸로 또 나머지 생성
        tilt(dir)
    for i in range(n):
        for j in range(n):
            mx = max(mx, board2[i][j])

print(mx)
