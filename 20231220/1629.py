# 1승을 계산할 수 있다.
# k승을 계산했으면 2k승과 2k+1승도 O(1)에 계산할 수 있다.

def POW(a,b,m):
    if b == 1:
        return a % m
    val = POW(a, b//2, m) #k승 계산
    val = val * val % m #2k승 계산
    if b % 2 == 0:
        return val
    return val * a % m

a, b, c = map(int, input())
print(POW(a,b,c))
