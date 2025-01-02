def check(col, row, num):
    for i in range(row, row+num):
        for j in range(col, col+num):
            if paper[i][j] != paper[row][col]:
                return False
    return True

def mainfunc(col,row,n):
    if check(col,row,n):
        cnt[paper[col][row]] += 1
        return
    else:
        num = n // 2 # 4
        for i in range(2):
            for j in range(2):
                mainfunc(i*num, j*num, num)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0]
mainfunc(n,n,n)

print(cnt[0])
print(cnt[1])