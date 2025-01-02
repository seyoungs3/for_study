def func(k):
    if k == m:
        print(*arr)  # *arr을 사용하여 리스트의 요소를 공백으로 구분하여 출력
        return

    for i in range(1, n + 1):
        if not isused[i]:
            arr[k] = i
            isused[i] = 1
            func(k + 1)
            isused[i] = 0

n, m = map(int, input().split())
arr = [0] * m
isused = [0] * (n + 1)

func(0)