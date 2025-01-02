def func(k):
    if k == m:
        for element in mat:
            print(element, end=' ')
        print()
        return
    for i in range(n):
        if not isused[i]:
            mat[k] = arr[i]
            isused[i] = 1
            func(k+1)
            isused[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
mat = [0]*m
isused = [0]*n
func(0)