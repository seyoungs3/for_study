n = int(input())

def is_apocalypse_number(num):
    num = str(num)
    return '666' in num

num = 666
count = 0
while True:
    if is_apocalypse_number(num) == True:
        count = count + 1
    
    if count == n:
        print(num)
        break
               
    num = num + 1