# 팰린드롬인지 확인하기

word = input()

length = len(word)
is_palindrome = 1
for i in range(int(length/2)):
    if word[i] != word[length-1-i]: # 다르면
        is_palindrome = 0
        break
print(is_palindrome)



