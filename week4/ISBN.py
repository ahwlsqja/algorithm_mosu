str_value = str(input())

sums = 0
indexss = 0

for i in range(0, len(str_value)):
    if str_value[i] != '*':
        if i % 2 == 0:
            sums += int(str_value[i])
        else:
            sums += 3 * int(str_value[i])
    
    if str_value[i] == '*':
        indexss = i

for i in range(0, 10):
    if indexss % 2 == 0:
        if (sums + i) % 10 == 0:
            print(i)
            break

    else:
        if (sums + 3 * i) % 10 == 0:
            print(i)
            break
         