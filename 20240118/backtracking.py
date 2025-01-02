# 지피티가 알려줬는데 잘 모르겠음 ㅠㅠ

def pick(m, cur):
    if m == cur:
        return [picked.copy()]  # 선택한 리스트의 복사본을 리스트로 반환
    result = []
    for i in range(l):
        if not isused[i]:
            picked[cur] = i
            isused[i] = True
            result += pick(m, cur + 1)
            isused[i] = False
    return result

l = 4
isused = [0 for _ in range(l)]
picked = [0 for _ in range(2)]
result = pick(2, 0)
print(result)
