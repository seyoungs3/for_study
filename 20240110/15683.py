import copy

def func(cur, n):
    global array
    if cur == n:
        arrays.append(array)
        return
    if loc[cur][0] == 1:
        for function in one:
            array = copy.deepcopy(room)
            function(loc[cur][1],loc[cur][2], array)
            func(cur+1, n)
    elif loc[cur][0] == 2:
        for function in two:
            array = copy.deepcopy(room)
            function(loc[cur][1],loc[cur][2], array)
            func(cur+1, n)
    elif loc[cur][0] == 3:
        for function in three:
            array = copy.deepcopy(room)
            function(loc[cur][1],loc[cur][2], array)
            func(cur+1, n)
    elif loc[cur][0] == 4:
        for function in four:
            array = copy.deepcopy(room)
            function(loc[cur][1],loc[cur][2], array)
            func(cur+1, n)
    elif loc[cur][0] == 5:
        for function in five:
            array = copy.deepcopy(room)
            function(loc[cur][1],loc[cur][2], array)
            func(cur+1, n)

def right(row, col, array):
    j = col+1
    while j!= lencol:
        if room[row][j] == 6:
            break
        array[row][j] = '#'
        j += 1

def left(row, col, array):
    j = col-1
    while j!= -1:
        if room[row][j] == 6:
            break
        array[row][j] = '#'
        j -= 1

def down(row, col, array):
    i = row+1
    while i!= lenrow:
        if room[i][col] == 6:
            break
        array[i][col] = '#'
        i += 1

def up(row, col, array):
    i = row-1
    while i!= -1:
        if room[i][col] == 6:
            break
        array[i][col] = '#'
        i-= 1

def two1(row, col, array):
    left(row, col, array)
    right(row, col, array)

def two2(row, col, array):
    up(row, col, array)
    down(row, col, array)

def three1(row, col):
    up(row, col)
    right(row, col)

def three2(row, col):
    right(row, col)
    down(row, col)

def three3(row, col):
    left(row, col)
    down(row, col)

def three4(row, col):
    left(row, col)
    up(row, col)

def four1(row, col):
    left(row, col)
    up(row, col)
    down(row, col)

def four2(row, col):
    up(row, col)
    right(row, col)
    down(row, col)

def four3(row, col):
    left(row, col)
    down(row, col)
    right(row, col)

def four4(row, col):
    left(row, col)
    up(row, col)
    down(row, col)

def five1(row, col):
    up(row, col)
    down(row, col)
    left(row, col)
    down(row, col)



lenrow, lencol = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(lenrow)]

one = [up, down, left, right]
two = [two1, two2]
three = [three1, three2, three3, three4]
four = [four1, four2, four3, four4]
five = [five1]

loc = []

for i in range(lenrow):
    for j in range(lencol):
        if room[i][j] == 1:
            loc.append([1,i,j])
        elif room[i][j] == 2:
            loc.append([2,i,j])
        elif room[i][j] == 3:
            loc.append([3,i,j])
        elif room[i][j] == 4:
            loc.append([4,i,j])
        elif room[i][j] == 5:
            loc.append([5,i,j])


arrays = []
n = len(loc)
func(0,n)
for array in arrays:
    print(array)