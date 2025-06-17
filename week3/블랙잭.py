a, b = map(int, input().split())
my_list = list(map(int, input().split()))
my_list.sort()  # 따로 정렬

max_sum = 0  # 초기값을 0으로

for i in range(a-2):        # 0부터 a-3까지
    for j in range(i+1, a-1):   # i+1부터 a-2까지  
        for k in range(j+1, a):     # j+1부터 a-1까지
            current_sum = my_list[i] + my_list[j] + my_list[k]
            if current_sum <= b and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)