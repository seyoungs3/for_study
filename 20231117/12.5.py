x = input().split()
y = map(float,input().split())

# lux = {a:b, b:c}

lux = dict(zip(list(x),list(y)))

print(lux)