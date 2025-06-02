# 백준 막대기 자르기 문제 해결
# 시간복잡도: O(log n * m) - n은 초기값 64, m은 리스트 길이(최대 log n)
# 공간복잡도: O(log n) - 최대 리스트 길이가 log n개

x = int(input())

n = 64
count = 1
stick_list = [64]

# list의 합이 x가 아닐 때
# 최악의 경우 O(log 64) = O(6)번 반복
while (n != x):
   # min() 함수: O(m), m은 현재 리스트 길이
   min_val = min(stick_list) // 2
   
   # remove(min()) 함수: O(m) - min 찾기 + 제거
   stick_list.remove(min(stick_list))
   
   # append() 함수: O(1) * 2
   stick_list.append(min_val)
   stick_list.append(min_val)

   # 조건 확인을 위한 임시 리스트 생성
   # copy(): O(m), 현재 리스트 복사
   temp_list = stick_list.copy()
   
   # remove(min()): O(m)
   temp_list.remove(min(temp_list))
   
   # sum(): O(m)
   if sum(temp_list) >= x:
       # remove(min()): O(m)
       stick_list.remove(min(stick_list))

   # sum(): O(m)
   n = sum(stick_list)

# 총 시간복잡도: O(log n * m) where m ≤ log n
# 총 공간복잡도: O(log n) - stick_list와 temp_list 저장공간
print(len(stick_list))