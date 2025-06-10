n = int(input())
for i in range(n):
    h, w, n = map(int, input().split())
    
    # 층수 계산: n번째 손님이 몇 층에 배정될지
    floor = ((n - 1) % h) + 1
    
    # 호수 계산: n번째 손님이 그 층의 몇 번째 방에 배정될지
    room_num = ((n - 1) // h) + 1
    
    # 방 번호 출력 (층수 + 호수)
    if room_num < 10:
        print(f"{floor}0{room_num}")
    else:
        print(f"{floor}{room_num:02d}")