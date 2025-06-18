while True:
    n = str(input())

    if int(n) == 0:
        break

    front = ""  # 변수 초기화
    back = ""
    
    if len(n) % 2 == 0:  # 짝수 길이
        # 앞쪽 절반
        for i in range(len(n)//2):
            front += n[i]
        
        # 뒤쪽 절반
        for j in range(len(n)//2, len(n)):
            back += n[j]
        
        reversed_back = back[::-1]
        
        if front == reversed_back:
            print('yes')
        else:
            print('no')
    
    else:  # 홀수 길이
        # 앞쪽 (가운데 제외)
        for i in range(len(n)//2):
            front += n[i]
        
        # 뒤쪽 (가운데 제외)
        for j in range(len(n)//2 + 1, len(n)):
            back += n[j]
        
        reversed_back = back[::-1]
        
        if front == reversed_back:
            print('yes')
        else:
            print('no')
