word = str(input())
result_list = []

# 첫 번째 구분점: 1부터 len(word)-2까지
for a in range(1, len(word)-1):
    # 두 번째 구분점: a+1부터 len(word)-1까지
    for b in range(a+1, len(word)):
        first = word[0:a]           # 처음부터 a까지
        second = word[a:b]          # a부터 b까지  
        third = word[b:len(word)]   # b부터 끝까지
        
        # 각각 뒤집기
        first_reversed = first[::-1]
        second_reversed = second[::-1]
        third_reversed = third[::-1]
        
        # 합치기
        joined_str = first_reversed + second_reversed + third_reversed
        result_list.append(joined_str)

print(sorted(result_list)[0])