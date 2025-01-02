# 2048 easy
# 한번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없음 (그림 12 참고)
# 블록이 추가되지는 않는다
# 똑같은 수가 세개 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐짐 (그림 14 15 참고)

# 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하라

# 보드의 크기 N
# N개의 줄 게임판의 초기상태
# 0은 빈칸, 이외의 값은 모두 블록
# 2보다 크고 1024보다 작은 2의 제곱수

# 시간복잡도
# 브루트 포스를 이용할 경우
# 4방향이니까 4**5 * 20 * 20 == 409600 -> 가능

# 생각해보니까 백트래킹임 (가지 뻗어가는 모양이니까)
# 한 방향에 대해서 시작
# 각 칸에 대해서 더할 수 있는지 확인 후 더할 수 있으면 더함
# 더할 수 있는 경우: 이동방향의 칸이 같은 경우
# 이동하려고 하는 쪽의 칸이 먼저 더해지는거 고려해야됨
# 그러면 이동방향 함수마다 더할수 있는지 여부 확인 함수내에 순서 변경이 필요함
# 더함 검사 함수 4개 만들어야됨(방향에 따라)
# 더함 검사 함수 내에 더함 함수도 구현
# 아 이동함수 만들어야됨,,,, 칸이 이동되잖슴
# 방향 함수에서 더할 수 있으면 더하고 못 더하면 이동시키면 됨

def up(inblock):
    outblock = [list(0 for _ in range(n)) for _ in range(n)]
    for j in range(n):
        cur = 0
        for i in range(n):
            if inblock[i][j] != 0:
                outblock[cur][j] = inblock[i][j]
                cur+=1
    for j in range(n):
        for i in range(n-1):
            if outblock[i][j] == outblock[i+1][j]:
                outblock[i][j] *= 2
                outblock[i+1][j] = 0
    return outblock           

def down(inblock):
    outblock = [list(0 for _ in range(n)) for _ in range(n)]
    for j in range(n):
        cur = n-1
        for i in range(n):
            if inblock[i][j] != 0:
                outblock[cur][j] = inblock[i][j]
                cur-=1
    for j in range(n):
        for i in range(n):
            if outblock[i][j] == outblock[i-1][j]:
                outblock[i][j] *= 2
                outblock[i-1][j] = 0
    return outblock

def left(array):
    arr = [0 for _ in range(n)]
    pre = 0
    idx = 0
    for i in range(len(array)):
        if array[i] == 0:
            continue
        if array[i] != 0:
            if array[i] != arr[pre]:
                arr[idx] = array[i]
                idx += 1
            if array[i] == arr[pre]:
                arr[pre] *= 2
                pre+=1
    return arr
        

n = int(input())
# block = [list(map(int, input().split())) for _ in range(n)]
# outblock = up(block)

# for line in outblock:
#     print(line)

array = list(map(int, input().split()))

ans = left(array)

print(ans)