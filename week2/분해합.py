n = int(input())
divided_num  = 0
abc = 0
flag = False
for a in range(n):
    divided_num += 1
    nums = str(divided_num)
    abc = 0
    for i in nums:
        abc += int(i)
    
    abc += divided_num

    if abc == n:
        flag = True
        break

if flag:
    print(divided_num)
else:
    print(0)