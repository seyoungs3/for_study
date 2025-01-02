# 트럭
# n개의 트럭
# w대의 트럭만 동시에 올라갈 수 있음
# 다리의 길이는 w
# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 최대하중 L보다 작거나 같아야 함
# 다리 위에 완전히 올라가지 못한 트럭은 무게합에 포함하지 않음

# 모든 트럭이 다리를 건너는 최단시간

# 트럭의 수 n, 다리의 길이 L, 다리의 최대하중 w

from collections import deque

n,L,w = map(int,input().split())
wtrucks = list(map(int, input().split()))
Q = deque([0 for _ in range(L-1)])
Q.append(wtrucks[0])
t = 1
sigma = sum(Q)
i = 1
while sigma != 0: # 무게가 0 -> 모두 다리를 지나갈 때 까지
    left = Q.popleft()
    sigma -= left
    if i < n:
        if sigma + wtrucks[i] <= w:
            Q.append(wtrucks[i])
            sigma += wtrucks[i]
            i += 1
        else:
            Q.append(0)
    else:
        Q.append(0)
    t += 1

print(t)

        