def func(cur, tot):
    global cnt
    if cur == n: # 끝까지 방문(넣을지 말지 결정) 했는데
        if tot == s: # 합이 같은 경우
            cnt += 1
        return
    func(cur+1, tot) # 다음 값을 더하지 않는 경우
    func(cur+1, tot + arr[cur]) # 다음 값을 더하는 경우
        


n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
func(0,0)

if s == 0:
    cnt -= 1

print(cnt)