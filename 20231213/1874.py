import sys
input = sys.stdin.readline

n = int(input())

A = [0]*n

for i in range(n):
    A[i] = int(input())

stack = []
number = 1
ans = []

for i in range(n):
    if number <= A[i]:
        while number <= A[i]:
            stack.append(number)
            number+=1
            ans.append('+')
        stack.pop()
        ans.append('-')
    else:
        a = stack.pop()
        if a > A[i]:
            ans =[]
            ans.append('NO')
            break
        else:
            ans.append('-')

if ans != 'NO':
    for i in ans:
        print(i)
else:
    print('NO')