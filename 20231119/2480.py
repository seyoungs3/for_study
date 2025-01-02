a,b,c = map(int, input().split())

if a==b==c:
    x = 10000+a*1000
elif a!=b and b!=c and a!=c:
    dice = [a,b,c]
    dice.sort()
    x = dice[-1]*100
else:
    if a == b:
        x = 1000+a*100
    elif a == c:
        x = 1000+a*100
    elif b == c:
        x = 1000+b*100

print(x)