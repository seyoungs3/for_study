a = [38,21,53,62,19]
for i in a:
    print(i)

for index, value in enumerate(a):
    print(index, value)

for index, value in enumerate(a, start=1):
    print(index, value)