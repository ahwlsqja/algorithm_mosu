a, b = map(int, input().split())

upper = 1
lower = 1
for i in range(a, a-b, -1):
    upper *= i

for j in range(b, 1, -1):
    lower *= j

print(int(upper/lower))