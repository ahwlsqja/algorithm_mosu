def solve_apartment(k, n):
    # dp[층][호수] = 해당 층, 호수에 사는 사람 수
    # 최대 14층, 14호까지 가능하므로 15x15 배열 생성
    dp = [[0] * 15 for _ in range(15)]
    
    # 0층 초기화: 0층의 i호에는 i명이 산다
    for i in range(1, 15):
        dp[0][i] = i
    
    # 1층부터 k층까지 계산
    for floor in range(1, k + 1):
        for room in range(1, 15):
            # 현재 층의 현재 호수 = 아래층의 1호부터 현재 호수까지의 합
            dp[floor][room] = dp[floor][room-1] + dp[floor-1][room]
    
    return dp[k][n]

# 테스트 케이스 처리
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(solve_apartment(k, n))