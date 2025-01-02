board = [input() for _ in range(4)]

def go(x, dir):
    dirs = [0] * 4
    dirs[x] = dir
    
    # 왼쪽으로 회전을 전파
    idx = x
    while idx > 0 and board[idx][6] != board[idx-1][2]:
        dirs[idx-1] = -dirs[idx]
        idx -= 1
    
    # 오른쪽으로 회전을 전파
    idx = x
    while idx < 3 and board[idx][2] != board[idx+1][6]:
        dirs[idx+1] = -dirs[idx]
        idx += 1

    for i in range(4):
        if dirs[i] == -1:
            board[i] = board[i][1:] + board[i][0]
        elif dirs[i] == 1:
            board[i] = board[i][-1] + board[i][:-1]

k = int(input())
for _ in range(k):
    x, dir = map(int, input().split())
    go(x - 1, dir)

ans = sum([(1 << i) if board[i][0] == '1' else 0 for i in range(4)])
print(ans)
