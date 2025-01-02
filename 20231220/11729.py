# n-1개의 원판을 옮길 수 있으면 n개의 원판을 옮길 수 있다

def func(a,b,n):
    if n == 1:
        print(a,b)
        return
    func(a, 6-a-b, n-1)
    print(a,b)
    func(6-a-b,b,n-1)

k = int(input())
print((1<<k)-1)
func(1,3,k)