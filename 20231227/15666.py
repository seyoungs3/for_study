def func(k):
    if k == m:
        for element in mat:
            print(element, end=' ')
        print()
        return
    
    for i in range(len(arr)):
        if not isused[i]:
            mat[k] = arr[i]
            for index in range(0,i):
                isused[index] = 1
            func(k+1)
        for index in range(0,i):
            isused[index] = 0
        
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
mat = [0]*m
isused = [0]*len(arr)

func(0)