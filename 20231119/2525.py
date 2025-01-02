a, b = map(int, input().split())
c = int(input())

x = b+c

while x >= 60:
    if x >= 60:
        a = a + 1
        x = x - 60
    else:
        break

if a >= 24:
    a = a-24 

print(a,x)