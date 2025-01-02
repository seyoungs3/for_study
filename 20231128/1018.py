n, m = map(int,input().split())

board = []
for i in range(n):
    line = []
    line = input()
    board.append(line)

text_W = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
text_B = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'

correctboard_W = [['']*8 for _ in range(8)]
k = 0
for i in range(8):
    for j in range(8):
        correctboard_W[i][j] = text_W[k]
        k = k+1

correctboard_B = [['']*8 for _ in range(8)]
k = 0
for i in range(8):
    for j in range(8):
        correctboard_B[i][j] = text_B[k]
        k = k+1

val = []
for i in range(n-7):
    for j in range(m-7):
        repaint_W = 0
        repaint_B = 0
        for row in range(8):
            for col in range(8):
                if board[i+row][j+col] != correctboard_W[row][col]:
                    repaint_W = repaint_W+1
        for row in range(8):
            for col in range(8):
                if board[i+row][j+col] != correctboard_B[row][col]:
                    repaint_B = repaint_B+1

        if repaint_W < repaint_B:
            repaint = repaint_W
        else:
            repaint = repaint_B    

        val.append(repaint)

print(min(val))

