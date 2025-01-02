import copy

def func(cur, n, room):
    global copied
    copied = copy.deepcopy(room)
    if cur == n:
        arrays.append(copied)
        return
    if loc[cur][0] == 1:
        for dir in one:
            changed = dir(loc[cur][1],loc[cur][2], copied)
            func(cur+1, n, changed)
            copied = copy.deepcopy(room)
    elif loc[cur][0] == 2:
        for dir in two:
            changed = dir(loc[cur][1],loc[cur][2], copied)
            func(cur+1, n, changed)
            copied = copy.deepcopy(room)
    elif loc[cur][0] == 3:
        for dir in three:
            changed = dir(loc[cur][1],loc[cur][2], copied)
            func(cur+1, n, changed)            
            copied = copy.deepcopy(room)
    elif loc[cur][0] == 4:
        for dir in four:
            changed = dir(loc[cur][1],loc[cur][2], copied)
            func(cur+1, n, changed)
            copied = copy.deepcopy(room)
    elif loc[cur][0] == 5:
        for dir in five:
            changed = dir(loc[cur][1],loc[cur][2], copied)
            func(cur+1, n, changed)
            copied = copy.deepcopy(room)

def right(row, col, array):
    j = col+1
    ans = copy.deepcopy(array)
    while j!= lencol:
        if room[row][j] == 6:
            break
        ans[row][j] = '#'
        j += 1
    return ans

def left(row, col, array):
    j = col-1
    ans = copy.deepcopy(array)
    while j!= -1:
        if room[row][j] == 6:
            break
        ans[row][j] = '#'
        j -= 1
    return ans

def down(row, col, array):
    i = row+1
    ans = copy.deepcopy(array)
    while i!= lenrow:
        if room[i][col] == 6:
            break
        ans[i][col] = '#'
        i += 1
    return ans

def up(row, col, array):
    i = row-1
    ans = copy.deepcopy(array)
    while i!= -1:
        if room[i][col] == 6:
            break
        ans[i][col] = '#'
        i-= 1
    return ans

def two1(row, col, array):
    mod = left(row, col, array)
    ans = right(row, col, mod)
    return ans

def two2(row, col, array):
    mod = up(row, col, array)
    ans = down(row, col, mod)
    return ans

def three1(row, col, array):
    mod = up(row, col, array)
    ans = right(row, col, mod)
    return ans

def three2(row, col, array):
    mod = right(row, col, array)
    ans = down(row, col, mod)
    return ans

def three3(row, col, array):
    mod = left(row, col, array)
    ans = down(row, col, mod)
    return ans

def three4(row, col, array):
    mod = left(row, col, array)
    ans = up(row, col, mod)
    return ans

def four1(row, col, array):
    mod = left(row, col, array)
    modd = up(row, col, mod)
    ans = down(row, col, modd)
    return ans

def four2(row, col, array):
    mod = up(row, col, array)
    modd = right(row, col, mod)
    ans = down(row, col, modd)
    return ans

def four3(row, col, array):
    mod = left(row, col, array)
    modd = down(row, col, mod)
    ans = right(row, col, modd)
    return ans

def four4(row, col, array):
    mod = left(row, col, array)
    modd = up(row, col, mod)
    ans = down(row, col, modd)
    return ans

def five1(row, col, array):
    mod = up(row, col, array)
    mod2 = down(row, col, mod)
    mod3 = left(row, col, mod2)
    ans = down(row, col, mod3)
    return ans


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
func(0,n,room)

# for copied in arrays:
#    for row in copied:
#       print(row)
#    print()

cnt = []
minimum = 500
for array in arrays:
    howmany = 0
    for i in range(lenrow):
        for j in range(lencol):
            if array[i][j] == 0:
                howmany += 1
    cnt.append(howmany)
    minimum = min(minimum, howmany)
    
print(minimum)
# print(cnt)