def func1(n):
    if n == 0:
        return
    print(n)
    func1(n-1)

def func2(n):
    if n == 0:
        return 0
    return n+func2(n-1)

func1(3)

a = func2(3)
print(a)