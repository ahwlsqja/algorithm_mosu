n = int(input())

for i in range(1, n+1):
    s = ""
    for j in range(1, n-i+1):
        s += " "
    for k in range(n-i+1, n+1):
        s += "*"
    print(s)