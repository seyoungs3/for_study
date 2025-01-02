import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

count = 0
imhere = [0 for _ in range(2000001)]
for i in arr:
    if i < x:
        imhere[i]+=1
    if i!= x-i and imhere[x-i]!=0:
            count+=1 
        
print(count)