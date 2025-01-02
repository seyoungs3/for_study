n, m = map(int,input().split())

board = []
for i in range(n):
    line = []
    line = input()
    board.append(line)

text_W = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
text_B = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'

correctboard_W = [[0]*8]*8
k = 0
for i in range(8):
    for j in range(8):
        correctboard_W[i][j] = text_W[k]
        k = k+1

correctboard_B = [[0]*8]*8
k = 0
for i in range(8):
    for j in range(8):
        correctboard_B[i][j] = text_B[k]
        k = k+1

repaint = 0
for i in range(n-7):
    for j in range(m-7):
        if board[i][j] == 'W':
            for row in range(8):
                for col in range(8):
                    if board[i+row][j+col] != correctboard_W[row][col]:
                        repaint = repaint+1
        if board[i][j] == 'B':
            for row in range(8):
                for col in range(8):
                    if board[i+row][j+col] != correctboard_B[row][col]:
                        repaint = repaint+1

print(repaint)