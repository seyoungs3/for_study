def attach(lrow,lcol,sticker):
    srow = len(sticker[0])
    scol = len(sticker)
    for i in range(lcol, lcol+scol):
        for j in range(lrow, lrow+srow):
            if i < 0 or i >= n or j < 0 or j >= m:
                continue
            if sticker[i-lcol][j-lrow] == 1:
                laptop[i][j] = 1 

n,m = map(int,input().split())
laptop = [list(0 for _ in range(m)) for _ in range(n)]
k = int(input())
sticker = [list(map(int, input().split())) for _ in range(k)]

attach(2,1,sticker)

for line in laptop:
    print(line)