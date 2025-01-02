# 리스트의 할당과 복사

a = [0,0,0,0,0]
b = a # ** a와 b는 같은 객체(a is b == True), 따라서 b의 요소를 변경하면 a에도 반영

b = a.copy() # 맞는 방법, (a is b == False, a == b)
