import sys
input = sys.stdin.readline

s, p = map(int, input().split()) # 문자열 길이 s, 부분 문자열 길이 p
dna = list(input())
needarr = map(int, input().split()) # 조건

# CCTGGATTG
j = 1+p
part = dna[1:j] # CCTG
answer = 0

countarr = []
countarr.append(part.count('a'))
countarr.append(part.count('c'))
countarr.append(part.count('g'))
countarr.append(part.count('t')) #[0 2 0 2]

while j < s:
    if countarr == needarr:
        answer += 1
    else:
        j += 1
        part.append(dna[j])
        if part[0] == 'a':
            countarr[0] -= 1
        if part[0] == 'c':
            countarr[1] -= 1
        if part[0] == 'g':
            countarr[2] -= 1
        if part[0] == 't':
            countarr[3] -= 1

        if dna[j] == 'a':
            countarr[0] += 1
        if dna[j] == 'c':
            countarr[1] += 1
        if dna[j] == 'g':
            countarr[2] += 1
        if dna[j] == 't':
            countarr[3] += 1
        del part[0]

print(answer)


