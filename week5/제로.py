N = int(input())

stack = []

for _ in range(N):
    a = int(input())

    if a == 0 and len(stack) != 0:
        stack.pop()
    else:
        stack.append(a)


print(sum(stack))
    
    
