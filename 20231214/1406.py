from collections import deque

string = list(input())
string = deque(string)

n = int(input())
for i in range(n):
    comment = list(input().split())
    if comment[0] == 'P':
        string.append(comment[1])
    elif comment[0] == 'L':
        