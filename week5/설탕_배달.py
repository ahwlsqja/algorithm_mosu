n = int(input())
count = 0

# 5kg 봉지를 최대한 많이 쓰기
while n > 0:
    if n % 5 == 0:  # 5로 나누어떨어지면 끝
        count += n // 5
        break
    elif n >= 3:    # 3kg 봉지 하나 사용
        n -= 3
        count += 1
    else:           # 만들 수 없음
        count = -1
        break

print(count)
