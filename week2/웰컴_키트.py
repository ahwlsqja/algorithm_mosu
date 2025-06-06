import math

# 입력 받기
N = int(input())
sizes = list(map(int, input().split()))  # S, M, L, XL, XXL, XXXL
T, P = map(int, input().split())

# 티셔츠 묶음 수 계산
# 각 사이즈별로 필요한 묶음 수를 계산하고 모두 더함
tshirt_bundles = 0
for size_count in sizes:
    if size_count > 0:
        # 올림 계산: (size_count + T - 1) // T 또는 math.ceil(size_count / T)
        tshirt_bundles += math.ceil(size_count / T)

# 펜 계산
# P자루씩 최대 몇 묶음 주문할 수 있는지 (몫)
pen_bundles = N // P
# 그 때 펜을 한 자루씩 몇 개 주문하는지 (나머지)
pen_individual = N % P

print(tshirt_bundles)
print(pen_bundles, pen_individual)