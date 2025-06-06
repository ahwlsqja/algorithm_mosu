while True:
    a, b, c = map(int, input().split())
    
    # 종료 조건
    if a == 0 and b == 0 and c == 0:
        break
    
    # 세 변을 정렬하여 가장 긴 변을 찾음
    sides = [a, b, c]
    sides.sort()
    
    # 피타고라스 정리: a² + b² = c² (c가 빗변)
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right")
    else:
        print("wrong")