from collections import deque

n = int(input())
cards = deque(range(1, n+1))  # [1, 2, 3, ..., n]

while len(cards) > 1:
    # 1단계: 맨 위 카드 버리기
    cards.popleft()
    
    # 2단계: 맨 위 카드를 맨 아래로
    if cards:  # 카드가 남아있다면
        top_card = cards.popleft()
        cards.append(top_card)

print(cards[0])
