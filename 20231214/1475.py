n = list(input())

count = [0 for _ in range(10)]
for i in n:
    i = int(i)
    count[i]+=1
    if i == 9:
        count[9]-=1
        count[6]+=1

if count[6] % 2 == 0:
    count[6] = int(count[6]/2)
else:
    count[6] = int((count[6]+1)/2)

mymax = count[0]
for i in count:
    if mymax < i:
        mymax = i
print(mymax)