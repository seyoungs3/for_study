def check(i, j, n):
    for row in range(i,i+n):
        for col in range(j,j+n):
            if board[i][j] != board[row][col]:
                return False
    return True
                
def solve(i,j,n):
    isSame = check(i,j,n)
    if isSame == True:
         numPaper[board[i][j]] += 1
         return
    else:
        n = n//2
        for k in range(2):
            for g in range(2):
                solve(i+k*n,j+g*n,n)



n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
numPaper = [0,0]
solve(0,0,n)
for num in numPaper:
     print(num)