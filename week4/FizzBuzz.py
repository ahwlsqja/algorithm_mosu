def solve_fizzbuzz():
    # 세 개의 입력 받기
    inputs = []
    for _ in range(3):
        inputs.append(input().strip())
    
    # 숫자인 것을 찾아서 다음 숫자 계산
    next_num = None
    
    for i in range(3):
        if inputs[i].isdigit():
            # i번째가 숫자라면, 그 다음 숫자는 inputs[i] + (3-i)
            current_num = int(inputs[i])
            next_num = current_num + (3 - i)
            break
    
    # 만약 모든 입력이 문자열이라면 (매우 드문 경우)
    # 이 경우 패턴을 분석해야 하는데, 문제에서는 보장하지 않음
    # 하지만 안전하게 처리
    if next_num is None:
        # 모든 경우가 Fizz, Buzz, FizzBuzz인 경우
        # 이런 경우는 매우 드물지만, 임의의 숫자로 시작
        next_num = 4  # 예시용
    
    # FizzBuzz 규칙 적용
    def fizzbuzz_convert(n):
        if n % 15 == 0:  # 3과 5의 배수
            return "FizzBuzz"
        elif n % 3 == 0:  # 3의 배수
            return "Fizz"
        elif n % 5 == 0:  # 5의 배수
            return "Buzz"
        else:
            return str(n)
    
    print(fizzbuzz_convert(next_num))

solve_fizzbuzz()