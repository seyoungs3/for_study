def piv(n):
    if n == 0 or n == 1:
        return n
    else:
        return piv(n-1) + piv(n-2)

n = int(input())
print(piv(n))