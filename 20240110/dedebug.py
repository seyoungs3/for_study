import copy

def func(cur, n):
    global temp
    if cur == 0:
        temp = copy.deepcopy(room)
    if cur == n:
        arrays.append(temp)
        return
    if loc[cur][0] == 1:
        for dir in one:
            prev = dir(loc[cur][1],loc[cur][2], temp)
            func(cur+1, n)
            temp = copy.deepcopy(prev)
    elif loc[cur][0] == 2:
        for dir in two:
            prev = dir(loc[cur][1],loc[cur][2], temp)
            func(cur+1, n)
            temp = copy.deepcopy(prev)


def right(row, col, temp):
    j = col+1
    while j!= lencol:
        if room[row][j] == 6:
            break
        temp[row][j] = 7
        j += 1
    return temp

def left(row, col, temp):
    j = col-1
    while j!= -1:
        if room[row][j] == 6:
            break
        temp[row][j] = 7
        j -= 1
    return temp

def down(row, col, temp):
    i = row+1
    while i!= lenrow:
        if room[i][col] == 6:
            break
        temp[i][col] = 7
        i += 1
    return temp

def up(row, col, temp):
    i = row-1
    while i!= -1:
        if room[i][col] == 6:
            break
        temp[i][col] = 7
        i-= 1
    return temp

def two1(row, col, temp):
    fixed = left(row, col, temp)
    array = right(row, col, fixed)
    return array

def two2(row, col, temp):
    fixed = up(row, col, temp)
    array = down(row, col, fixed)
    return array


lenrow, lencol = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(lenrow)]

one = [up, down, left, right]
two = [two1, two2]

loc = []

for i in range(lenrow):
    for j in range(lencol):
        if room[i][j] == 1:
            loc.append([1,i,j])
        elif room[i][j] == 2:
            loc.append([2,i,j])


arrays = []
n = len(loc) - 1 
func(0,n)
for temp in arrays:
    print(temp)