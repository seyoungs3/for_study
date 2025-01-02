# 스티커 붙이기
# 1 스티커를 회전시키지 않음
# 2 다른 스티커와 겹치거나 노트북을 벗어나지 않아야함, 노트북의 위쪽부터, 위쪽 여러곳이면 가장 왼쪽 위치
# 3 스티커를 붙이지 못하면 90도 회전, 180도, 270도 회전해서 시도
# 4 그래도 안되면 버림
# 스티커를 노트북에 차례대로 붙였을 때 스티커가 붙은 칸의 개수 출력

# 회전하는 함수 만들기
# 회전 함수는 90도 회전을 반복함으로써 전부 만들 수 있음
# 스티커 붙일 수 있는지 판단(상단 왼쪽부터 확인) 0,0부터 n,m까지
# 스티커 붙일 수 있으면 노트북에 추가
# 모든 스티커 진행하면 배열 확인 후 출력

def okay(lrow,lcol,sticker):
    srow = len(sticker[0])
    scol = len(sticker)
    for i in range(lcol, lcol+scol):
        for j in range(lrow, lrow+srow): # 시작점이 너무 뒤쪽이면 스티커 못붙이자나! 그거 처리 안했음 -> 함
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if laptop[i][j] == 1:
                if sticker[i-lcol][j-lrow] == 1:
                    return False
    return True

def rotate90(sticker):
    srow = len(sticker[0])
    scol = len(sticker)
    new = [list(0 for _ in range(scol)) for _ in range(srow)]       
    for i in range(scol):
        for j in range(srow):
            if sticker[i][j] == 1:
                new[j][scol-i-1] = 1
    sticker[:] = new[:]
 
def attach(lrow,lcol,sticker):
    srow = len(sticker[0])
    scol = len(sticker)
    for i in range(lcol, lcol+scol):
        for j in range(lrow, lrow+srow):
            if i < 0 or i >= n or j < 0 or j >= m:
                continue
            if sticker[i-lcol][j-lrow] == 1:
                laptop[i][j] = 1 # 저기요 잘못쓰셨는데요 지금 attach가 하나도 안되게 생겼는데요 -> 처리 완

n,m,s = map(int,input().split()) # 노트북 세로, 가로, 스티커 수
stickers = []
laptop = [list(0 for _ in range(m)) for _ in range(n)]
for _ in range(s):
    row, col = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(row)]
    stickers.append(sticker)

for sticker in stickers:
    finish = False
    for r in range(4): # 3번 회전
        for i in range(n):
            for j in range(m):
                if okay(i,j,sticker):
                    attach(i,j,sticker)
                    finish = True # 다음 스티커로 넘어가야됨
                    break
            if finish:
                break
        if finish:
            break
        else:
            rotate90(sticker)

for line in laptop:
    print(line)


cnt = 0
for line in laptop:
    for num in line:
        if num == 1:
            cnt+=1

print(cnt)
    

# TODO
# 아악 마지막 예제 입력8만 안됨 엉엉ㅇ엉 하기시렁