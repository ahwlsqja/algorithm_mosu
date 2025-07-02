n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda x: (x[1], x[0]))

for x, y in points:
    print(x, y)
