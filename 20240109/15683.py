def right(row, col):
    j = col
    while j!= m:
        if room[row][j] == 6:
            break
        room[row][j] = 1
        j += 1

def left(row, col):
    j = col
    while j!= 0:
        if room[row][j] == 6:
            break
        room[row][j] = 1
        j -= 1

def down(row, col):
    i = row
    while i!= n:
        if room[i][col] == 6:
            break
        room[i][col] = 1
        i += 1

def up(row, col):
    i = row
    while i!= 0:
        if room[i][col] == 6:
            break
        room[i][col] = 1
        i-= 1

def two1(row, col):
    left(row, col)
    right(row, col)

def two2(row, col):
    up(row, col)
    down(row, col)

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


n, m = map(int, input().split())
room = [list(map(int, input().split)) for _ in range(n)]

one = [up, down, left, right]
two = [two1, two2]
three = [three1, three2, three3, three4]
four = [four1, four2, four3, four4]
five = [five1]

onerow = []
onecol = []
tworow = []
twocol = []
threerow = []
threecol = []
fourrow = []
fourcol = []
fiverow = []
fivecol = []

for i in range(n):
    for j in range(m):
        if room[i][j] == 1:
            onerow.append(i)
            onecol.append(j)
        elif room[i][j] == 2:
            tworow.append(i)
            twocol.append(j)
        elif room[i][j] == 3:
            threerow.append(i)
            threecol.append(j)
        elif room[i][j] == 4:
            fourrow.append(i)
            fourcol.append(j)
        elif room[i][j] == 5:
            fiverow.append(i)
            fivecol.append(j)

for row in onerow:
    for col in onecol:
        