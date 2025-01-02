def order(cur):
    if cur == 5:
        print(arr)
        return
    for i in range(5):
        if isused[i] == 0:
            arr[cur] = i
            isused[i] = 1
            order(cur+1)
            isused[i] = 0


isused = [0 for _ in range(5)]
arr = [0 for _ in range(5)]
cur = 0
order(0)