import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001  # 값의 범위가 0~10000이라고 가정

for _ in range(n):
    k = int(input())
    count[k] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)