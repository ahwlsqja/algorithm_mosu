num1 = int(input())
num2 = int(input())
num3 = int(input())

answer = str(num1 * num2 * num3)

digit_count = {str(i): 0 for i in range(10)}
    
# 문자열의 각 숫자 카운팅
for digit in answer:
    if digit in digit_count:  # 숫자인 경우만 카운팅
        digit_count[digit] += 1

for digit in digit_count:
    print(digit_count[digit])