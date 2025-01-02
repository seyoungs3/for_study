n, m = map(int,input().split())

arr = list(range(1,n+1))

for i in range(m):
    a, b = map(int, input().split())
    cut = arr[a-1:b]
    del arr[a-1:b]
    cut.reverse()
    arr[a-1:a-1] = cut

for i in arr:
    print(i, end=' ')
