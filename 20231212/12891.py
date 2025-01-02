def myadd(letter):
    global acgtcount
    if letter == 'A':
        acgtcount[0]+=1
    elif letter == 'C':
        acgtcount[1]+=1
    elif letter == 'G':
        acgtcount[2]+=1
    elif letter == 'T':
        acgtcount[3]+=1

def mydel(letter):
    global acgtcount
    if letter == 'A':
        acgtcount[0]-=1
    elif letter == 'C':
        acgtcount[1]-=1
    elif letter == 'G':
        acgtcount[2]-=1
    elif letter == 'T':
        acgtcount[3]-=1

import sys
input = sys.stdin.readline

s, p = map(int, input().split()) # 전체 문자열 길이 s, 부분 문자열 길이 p
dna = list(input())
needarr = list(map(int, input().split()))

answer = 0
acgtcount = [0,0,0,0]

start = 0
for index in range(start,start+p):
    myadd(dna[index])

if acgtcount[0] >= needarr[0]:
    if acgtcount[1] >= needarr[1]:
        if acgtcount[2] >= needarr[2]:
            if acgtcount[3] >= needarr[3]:
                answer +=1

end = start+p-1
for end in range(end, s-1):
    myadd(dna[end+1])
    mydel(dna[start])
    
    if acgtcount[0] >= needarr[0]:
        if acgtcount[1] >= needarr[1]:
            if acgtcount[2] >= needarr[2]:
                if acgtcount[3] >= needarr[3]:
                    answer +=1
    start +=1

print(answer)




