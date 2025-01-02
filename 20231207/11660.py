import sys
input = sys.stdin.readline

n, m = map(int,input().split())

arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

presum = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        presum[i][j] = presum[i][j-1]+presum[i-1][j]-presum[i-1][j-1]+arr[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    answer = presum[x2][y2]-presum[x2][y1-1]-presum[x1-1][y2]+presum[x1-1][y1-1]
    print(answer)
    
