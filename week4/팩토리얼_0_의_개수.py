n = int(input())

count = 0
power_of_5 = 5

# 5의 거듭제곱으로 나누면서 개수를 센다
while power_of_5 <= n:
    count += n // power_of_5
    power_of_5 *= 5

print(count)