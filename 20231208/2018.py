n = int(input())

start = 1
end = 1
count = 1
sum = 1

while end!=n:
    if sum == n:
        count += 1
        end += 1
        sum += end
    elif sum < n:
        end += 1
        sum = sum + end
    elif sum > n:
        sum = sum - start # 실행 순서 매우 중요
        start += 1
        
print(count)
