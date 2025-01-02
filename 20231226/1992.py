def check(i, j, n):
    for row in range(i, i + n):
        for col in range(j, j + n):
            if pic[i][j] != pic[row][col]:  # Incorrect: should use pic[row][col]
                return False
    return True


def solve(i, j, n):
    isSame = check(i, j, n)
    if isSame == True:
        ans.append(pic[i][j])
    else:
        ans.append('(')
        n = n // 2
        solve(i, j, n)
        solve(i, j + n, n)
        solve(i + n, j, n)
        solve(i + n, j + n, n)
        ans.append(')')

n = int(input())
pic = [list(input()) for _ in range(n)]
ans = []
solve(0, 0, n)

for i in ans:
    print(i, end='')

