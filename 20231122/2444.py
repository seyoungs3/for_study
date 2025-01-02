n = int(input())

for i in range(n):
    for j in range(2*n-1):
        if n-1-i<=j<=n-1+i:
            print('*', end='')
        else:
            if n-1+i < j:
                print('', end='')
            else:
                print(' ',end='')
    
    print()

for i in range(n-1):
    for j in range(2*n-1):
        if i+1 <= j <= 2*n-3-i:
            print('*', end='')
        else:
            if 2*n-3-i < j:
                print('', end='')
            else:
                print(' ', end='')
    print()
    