n = int(input())
people = []

# 모든 사람의 몸무게와 키 입력받기
for i in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

ranks = []

# 각 사람에 대해 등수 계산
for i in range(n):
    rank = 1  # 기본 등수는 1등
    my_weight, my_height = people[i]
    
    # 다른 모든 사람과 비교
    for j in range(n):
        if i != j:  # 자기 자신과는 비교하지 않음
            other_weight, other_height = people[j]
            
            # 상대방이 나보다 덩치가 크면 등수 증가
            if other_weight > my_weight and other_height > my_height:
                rank += 1
    
    ranks.append(rank)

# 결과 출력
print(*ranks)
