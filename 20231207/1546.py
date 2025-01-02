n = int(input())

score_arr = list(map(int, input().split()))

m = max(score_arr)

sum = 0
for score in score_arr:
    score = score/m*100
    sum = sum + score

print(sum/n)