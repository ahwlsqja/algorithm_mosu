n = int(input())

fir = 666
s_count = 0
real_num = 666

for d in range(2, n+1):
    while s_count < 3 :
        s_count = 0
        fir += 1
        for k in str(fir):
            if k == '6':
                s_count += 1

    if s_count == 3:
        fir += 1
        s_count = 0
    
    real_num = fir

print(real_num -1)
