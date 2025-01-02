h = int(input())

for i in range(h):
    for j in range(2*h-1):
        if h-1-i <= j <= h-1+i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
