# 단어 공부

word = input()
word = word.upper()

length = len(word)

howmany = [0] * length
for i in range(length):
    howmany[i] = word[i].count #첫번째부터 마지막까지 각각 개수 세기

if max(howmany) < int(howmany.count(max(howmany))):
    print('?')
elif max(howmany) == int(howmany.count(max(howmany))):
    where = index(max(howmany))
    print(word[where])
else:
    print('error')
