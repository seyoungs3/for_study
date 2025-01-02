def solve(n, x, y):
    if n == 1:
        board[x][y] = '*'
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            solve(n // 3, x + n // 3 * i, y + n // 3 * j)

n = int(input())
board = [[' ' for _ in range(n)] for _ in range(n)]

solve(n, 0, 0)

for i in range(n):
    print(''.join(board[i]))
