# 5*5 크기의 판 5개
# 하얀 칸은 들어갈 수 있고, 검은 칸은 들어갈 수 없음
# 시계 혹은 반시계 방향으로 회전 가능
# 회전 후 판 5개를 자유로운 순서로 쌓는다

# 현재 위치한 칸에서 면으로 인접한 칸이 하얀색인 경우 그 칸으로 이동 가능
# 본인이 설계한 미로를 가장 적은 이동 횟수로 탈출하면 우승
# 미로의 입구나 출구가 막혀있거나, 입구에서 출구에 도달할 수 있는 방법이 없으면 탈출 불가능

# 주어진 판에서 가장 적은 이동 횟수로 출구에 도달할 수 있게 했을 때 몇 번 이동을 해야하는지 구하기

# 탈출이 불가능할 경우에는 -1 출력

# 브루트 포스
# 백트래킹

def rotate(board): # 시계방향으로 90도 회전
    temp = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[i][j] = board[4-j][i] # 아직 temp에서 board로 복사 안함, 원본 보드 어케 해야될지 몰라서 보류중

def order(cur):
    if cur == 5:
        # TODO
        return
    for i in range(5):
        if isused[i] == 0:
            arr[cur] = i
            isused[i] = 1
            order(cur+1)
            isused[i] = 0


isused = [0 for _ in range(5)]
arr = [0 for _ in range(5)]
cur = 0
order(0)

        
    


    
    
    

boards = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

