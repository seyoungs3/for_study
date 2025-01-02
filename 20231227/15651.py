def func(k):
    if k == m:
        for element in mat:
            print(element, end= ' ')
        print()
        return
    for i in range(n):
        mat[k] = arr[i]
        func(k+1)

n, m = map(int, input().split())
arr = list(range(1,n+1))
mat = [0]*m
isused = [0]*n
func(0)