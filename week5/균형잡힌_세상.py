'''
원래 아무것도 없을때에도 append할 수 있다. 
'''
while(True):
    s = input()
    if s == '.':
        break
    stack = []
    for i in range(len(s)):
        if (s[i] == '(') or (s[i] == '['):
            stack.append(s[i])
        elif (s[i] == ')'):
            if (len(stack) != 0) and (stack[-1] == '('):
                stack.pop()
            else:
                stack.append(s[i])
                break
        elif (s[i] == ']'):
            if (stack[-1] == '[') and (len(stack) != 0):
                stack.pop()
            else:
                stack.append(s[i])
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")

            
