n = int(input())
for i in range(0, n):
    a, b = input().split(' ')
    s = ''
    for i in b:
        for k in range(0, int(a)):
            s += i
    print(s)


