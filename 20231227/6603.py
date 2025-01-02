def func(r):
    if r == 6:
        for element in mat:
            print(element, end = ' ')
        print()
        return
    for i in range(len(arr)):
        if not isused[i]:
            mat[r] = arr[i]
            for index in range(i+1):
                isused[index] = 1
            func(r+1)
            for index in range(i+1):
                isused[index] = 0

while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    k = arr.pop(0)
    mat = [0]*6
    isused = [0]*k
    func(0)
    print()
    
