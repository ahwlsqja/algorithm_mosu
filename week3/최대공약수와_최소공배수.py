a, b = map(int, input().split())

# 최대공약수 구하기
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

gcd_val = gcd(a, b)
lcm_val = a * b // gcd_val

print(gcd_val)
print(lcm_val)