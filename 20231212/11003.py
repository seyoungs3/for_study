from collections import deque
n, l = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(n):
    while mydeque and mydeque[-1][1] > now[i]: # 요소 있고 크면
        mydeque.pop()
    mydeque.append((i, now[i]))
    
    while mydeque and mydeque[0][0] < i-l+1:
        mydeque.popleft()
    
    print(mydeque[0][1], end=' ')
