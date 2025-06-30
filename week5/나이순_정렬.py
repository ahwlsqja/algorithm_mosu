N = int(input())
members = []

for i in range(N):
    age, name = input().split()
    age = int(age)  # 나이를 정수로 변환
    members.append((age, i, name))  # (나이, 가입순서, 이름) 튜플로 저장

# 나이 순으로 정렬, 나이가 같으면 가입 순서(i)로 정렬
members.sort(key=lambda x: (x[0], x[1]))

# 결과 출력
for age, _, name in members:
    print(age, name)