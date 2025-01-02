while True:
    a = input()
    stack = []
    
    if a == '.':
        break

    for i in a:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack)!=0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if len(stack)!=0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        print('yes')
    else:
        print('no')