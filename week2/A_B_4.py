# 방법 1: try-except 사용
try:
    while True:
        a, b = map(int, input().split())
        print(a + b)
except EOFError:
    pass