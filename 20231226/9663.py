def func(cur):
    global cnt
    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if isused1[i] or isused2[i + cur] or isused3[cur - i + n - 1]:
            continue

        isused1[i] = 1
        isused2[i + cur] = 1
        isused3[cur - i + n - 1] = 1
        func(cur + 1)
        isused1[i] = 0
        isused2[i + cur] = 0
        isused3[cur - i + n - 1] = 0

n = int(input())
isused1 = [0] * 40
isused2 = [0] * 40
isused3 = [0] * 40
cnt = 0

func(0)
print(cnt)
