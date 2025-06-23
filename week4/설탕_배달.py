N = int(input())
count = 0 #3을 뺀 횟수

while(N>=0):
    if N % 5 == 0:
        print(count + N//5)
        break
    N = N - 3
    count += 1
        
else: 
    print(-1)


