def func(k):
    if k == m:
        for element in mat:
            print(element, end=' ')
        print()
        return
    for i in range(n):
        if not isused[i]:
            mat[k] = arr[i]
            for j in range(0,i):
                isused[j] = 1
            func(k+1)
            for j in range(0,i):
                isused[j] = 0


n, m = map(int, input().split())
arr = list(range(1,n+1))
mat = [0]*m
isused = [0]*n
func(0)