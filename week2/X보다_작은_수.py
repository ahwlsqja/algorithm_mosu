a, b = map(int, input().split())
li = list(map(int, input().split()))

for i in range(0, a, 1):
    if(b > li[i]):
        print(li[i], end=' ')