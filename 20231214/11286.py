n = int(input())

arr = []

# 절댓값 가장 작은 값을 계속 갱신

for i in range(n):
    order = int(input())
    if order != 0:
        arr.append(order)
    else:
        if len(arr) == 0:
            print('0')
        else:
            print(arr[0])