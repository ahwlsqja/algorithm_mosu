n = int(input())

for i in range(0, n):
    aa = input().split('X')
    sums = 0
    for k in aa:
        for ii in range(1, len(k)+1):
            sums += ii
    print(sums)
    