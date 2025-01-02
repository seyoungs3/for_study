x = int(input()) # 줄의 갯수

for i in range(x):
    for j in range(x):
        if j <= i:
            print("*", end="")
    print()