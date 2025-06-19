A, B, V = map(int, input().split())

# 예외 처리: A가 V 이상이면 1일만에 완료
if A >= V:
    print(1)
else:
    # A > B인 경우에만 정상 작동
    if A > B:
        # 마지막 날 전까지 필요한 일수 계산
        # (V - A)를 (A - B)로 나눈 값의 올림
        import math
        days = math.ceil((V - A) / (A - B)) + 1
        print(days)
    else:
        # A <= B인 경우, 목표에 도달할 수 없음
        print(-1)  # 또는 적절한 에러 처리