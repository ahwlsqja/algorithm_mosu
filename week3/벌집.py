import math

def solve_beehive(n):
    """
    벌집에서 1번 방부터 n번 방까지의 최단거리를 구하는 함수
    
    벌집 구조 (거리 관점):
    - 거리 1: 1번 방 (중앙) - 1개
    - 거리 2: 2~7번 방 (1번째 링) - 6개  
    - 거리 3: 8~19번 방 (2번째 링) - 12개
    - 거리 k+1: k번째 링까지 총 방 개수: 3k² + 3k + 1
    """
    if n == 1:
        return 1
    
    # 더 안전한 방법: 직접 계산
    distance = 1
    total_rooms = 1
    
    while total_rooms < n:
        distance += 1
        total_rooms += 6 * (distance - 1)  # (distance-1)번째 링에 6*(distance-1)개 방
    
    return distance

# 테스트
n = int(input())
print(solve_beehive(n))