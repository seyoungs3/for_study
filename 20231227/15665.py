def func(k):
    if k == m:
        for element in mat:
            print(element, end=' ')
        print()
        return
    for i in range(len(arr)):
        mat[k] = arr[i]
        func(k+1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
mat = [0] * m
arr = list(set(arr))
arr.sort()

func(0)