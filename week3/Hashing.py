n = int(input())
a = input()

M = 1234567891  # 모듈로 값
r = 31          # 거듭제곱 밑

hash_value = 0

for i in range(len(a)):
    num = ord(a[i]) - ord('a') + 1
    hash_value += num * (r ** i)
    hash_value %= M  # 매번 모듈로 연산

print(hash_value)