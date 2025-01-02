def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def solve(x, y, z):
    if check(x, y, z): # True
        cnt[paper[x][y] + 1] += 1
        return
    n = z // 3
    for i in range(3):
        for j in range(3):
            solve(x + i * n, y + j * n, n)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0, 0]  # -1, 0, 1로 채워진 종이 갯수

solve(0, 0, N)

for i in range(3):
    print(cnt[i])

