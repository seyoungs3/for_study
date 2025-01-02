def func(k): # k개까지 수를 골랐음
    if k == m: # 다 골랐으면
        for i in mat:
            print(i, end= ' ')
        print()
        return
    for i in range(n):
        if not isused[i]: # 아직 사용되지 않았으면
            mat[k] = arr[i] # k번째 수는 arr[i]
            for index in range(0,i+1):
                isused[index] = 1
            func(k+1)
            for index in range(0,i+1):
                isused[index] = 0

n, m = map(int, input().split()) 
arr = list(range(1,n+1)) # [1,2,3,n]
isused = [0]*n #[0,0,0,0]
mat = [0]*m
func(0)

