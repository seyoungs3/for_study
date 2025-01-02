a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
mul = list(str(mul))

count = [0 for _ in range(10)]
for i in mul:
    i = int(i)
    count[i]+=1    

for i in count:
    print(i)