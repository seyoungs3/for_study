n = int(input())

timearr = []
for i in range(n):
    line = list(map(int,input().split()))
    timearr.append(line)

timearr.sort

print(timearr)