from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))
count_dict = Counter(numbers)

m = int(input())
queries = list(map(int, input().split()))

# 각 쿼리에 대해 카운트 출력
result = []
for query in queries:
    result.append(str(count_dict[query]))  # Counter는 없는 키에 대해 0을 반환

print(' '.join(result))