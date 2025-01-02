# 주사위 굴리기

# 이동한 칸에 0 -> 주사위 밑면 숫자가 칸에 복사
# 칸이 0 아님 -> 칸의 숫자가 주사위 밑면으로 복사, 칸 값을 0으로 변경
# 지도 바깥으로 이동시키려고 하는 명령 무시, 출력도 x

# 지도 세로 n, 지도 가로 m, 주사위 좌표 x,y, 명령의 개수 k
# 주사위를 놓은 칸에 쓰여 있는 수는 항상 0
# 지도의 각 칸에 쓰여 있는 수는 0~9
# 이동명령 동1 서2 북3 남4

# 주사위의 윗 면에 쓰여 있는 수 출력


def move(dir):
    global x, y
    movable = False
    temp = []
    if dir == 1:
        if y+1 < m:
            movable = True
            y += 1
            idxs = [3,1,0,5,4,2]
    elif dir == 2:
        if y-1 >= 0:
            movable = True
            y -= 1
            idxs = [2,1,5,0,4,3]          
    elif dir == 3:
        if x-1 >= 0:
            movable = True
            x-=1
            idxs = [4,0,2,3,5,1]  
    elif dir == 4:
        if x+1 < n:
            movable = True
            x+=1
            idxs = [1,5,2,3,0,4]

    if movable == True:
        for idx in idxs:
            temp.append(dice[idx])
        dice[:] = temp[:]

    return movable

def nummod():
    if mapp[x][y] == 0:
        mapp[x][y] = dice[5]
    elif mapp[x][y] != 0:
        dice[5] = mapp[x][y]
        mapp[x][y] = 0

n,m,x,y,k = map(int, input().split())
mapp = []
for _ in range(n):
    mapp.append(list(map(int, input().split())))
directions = list(map(int, input().split()))
dice = [0,0,0,0,0,0]
for dir in directions:
    movable = move(dir)
    if movable:
        nummod()
        print(dice[0])
    