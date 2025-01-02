a,b = map(int, input().split())

x = []

for i in range(a,b+1):
    x.append(2**i)

del x[1]
del x[-2]

print(x)