a=[]

for i in range(5):
    line=[]
    line = input()
    a.append(line)

for j in range(15):
    for i in range(5):
        try:
            print(a[i][j],end='')
        except:
            continue