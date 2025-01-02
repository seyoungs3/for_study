# 톱니바퀴
# 8개의 톱니(N극 or S극)를 가지고 있는 톱니바퀴 4개 -> 1,2,3,4번
# 맞닿은게 다르면 반대로 회전

# 톱니바퀴의 상태 4줄
# 12시방향부터 시계방향 순서로 N은 0, S는 1
# 다섯째 줄 회전횟수 K
# 톱니바퀴 번호, 방향(1은 시계, -1은 반시계)

# 점수의 합 출력

gears = [list(map(int, input())) for _ in range(4)]

def judge(num):
    if num == 1:       
        if gears[1][6] != gears[0][2]:
            rotatable[1] = True
            if gears[2][6] != gears[1][2]:
                rotatable[2] = True
                if gears[3][6] != gears[2][2]:
                    rotatable[3] = True
        if rotatable[1]:
            dir[1] = dir[0]*-1
            if rotatable[2]:
                dir[2] = dir[1]*-1
                if rotatable[3]:
                    dir[3] = dir[2]*-1

    elif num == 2:
        if gears[0][2] != gears[1][6]:
            rotatable[0] = True
        if gears[2][6] != gears[1][2]:
            rotatable[2] = True
            if gears[3][6] != gears[2][2]:
                rotatable[3] = True
        if rotatable[0]:
            dir[0] = dir[1]*-1
        if rotatable[2]:
            dir[2] = dir[1]*-1
            if rotatable[3]:
                dir[3] = dir[2]*-1

    elif num == 3:
        if gears[1][2] != gears[2][6]:
            rotatable[1] = True
            if gears[0][2] != gears[1][6]:
                rotatable[0] = True
        if gears[3][6] != gears[2][2]:
            rotatable[3] = True
        if rotatable[1]:
            dir[1] = dir[2]*-1
            if rotatable[0]:
                dir[0] = dir[1]*-1
        if rotatable[3]:
            dir[3] = dir[2]*-1

    elif num == 4:
        if gears[2][2] != gears[3][6]:
            rotatable[2] = True
            if gears[1][2] != gears[2][6]:
                rotatable[1] = True
                if gears[0][2] != gears[1][6]:
                    rotatable[0] = True
        if rotatable[2]:
            dir[2] = dir[3]*-1
            if rotatable[1]:
                dir[1] = dir[2]*-1
                if rotatable[0]:
                    dir[0] = dir[1]*-1

def roll(numgear,isrot, direction):
    if isrot: # 회전할 수 있는 경우에만 덮어쓰기
        temp = []
        if direction == 1: # 시계
            temp.append(gears[numgear][7])
            for idx in range(7):
                temp.append(gears[numgear][idx])
            gears[numgear][:] = temp[:] # 임시값 덮어쓰기
        elif direction == -1: # 반시계
            for idx in range(1,8):
                temp.append(gears[numgear][idx])
            temp.append(gears[numgear][0])
            gears[numgear][:] = temp[:] # 임시값 덮어쓰기
        else:
            print('direction unjudge error') # 회전할 수 있는데 dir이 0인 경우 -> ???

k = int(input())
for _ in range(k):
    num, d = map(int, input().split())
    rotatable = [False for _ in range(4)]
    dir = [0 for _ in range(4)]
    rotatable[num-1] = True
    dir[num-1] = d
    judge(num)
    for gearnum in range(4):
        roll(gearnum, rotatable[gearnum], dir[gearnum])

score = 0
if gears[0][0] == 1:
    score += 1
if gears[1][0] == 1:
    score += 2
if gears[2][0] == 1:
    score += 4
if gears[3][0] == 1:
    score += 8

# 정답 출력
print(score)