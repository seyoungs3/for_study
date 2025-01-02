# 치킨 배달
# 치킨 거리 = 가장 가까운 치킨집까지의 거리(맨하탄 거리)
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# 0은 빈칸, 1은 집, 2는 치킨집
# 도시의 치킨 거리가 최소가 되게 하는 치킨집 m개 선택

# 치킨집 m개 선택하는 함수
# 인덱스 선택

def pick(m, cur):
    if m == cur:
        return
    for i in range(l):
        if not isused[i]: # 안썼으면 추가 할 수 있음
            picked[cur] = i
            isused[i] = True
            pick(m, cur+1)
            isused[i] = False
    

n, m = map(int, input().split())
for _ in range(n):
    city = [list(map(int,input().split())) for _ in range(n)]

chickens = []
citychid = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            chickens.append([i,j])

l = len(chickens)

isused = [0 for _ in range(l)]
picked = []
pick(m,0)
chid = []
for i in range(n):
    for j in range(n):
        if city[i][j] != 1:
            continue
        if city[i][j] == 1: # 집 발견
            mn = 2*n # 최대값으로 일단 초기화
            for x,y in chickens: # 치킨집마다 시도
                d = abs(i-x)+abs(j-y)
                mn = min(mn, d) # 최솟값(치킨거리) 찾기
            chid.append(mn) # 치킨거리 저장
citychid.append(sum(chid)) # 도시 치킨거리 저장