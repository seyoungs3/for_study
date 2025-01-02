import copy

def func(cur, n):
    global array
    if cur == n:
        arrays.append(array)
        return
    for dir in one:
        array = room[:]
        dir(loc[cur][1], loc[cur][2])
        func(cur+1, n)



lenrow, lencol = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(lenrow)]

one = [up, down, left, right]

loc = []

for i in range(lenrow):
    for j in range(lencol):
        if room[i][j] == 1:
            loc.append([1,i,j])

arrays = []
n = len(loc)
func(0,n)
for array in arrays:
    print(array)
    print()
