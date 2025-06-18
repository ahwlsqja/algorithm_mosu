n = int(input())
scores = list(map(int, input().split()))

M = max(scores)
new_average = sum(score / M * 100 for score in scores) / n

print(new_average)