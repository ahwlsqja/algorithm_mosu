def is_balanced(s):
    """
    문자열이 균형잡힌 괄호를 가지는지 확인하는 함수
    """
    stack = []
    
    # 괄호 쌍 정의
    pairs = {')': '(', ']': '['}
    
    for char in s:
        # 열린 괄호인 경우 스택에 추가
        if char in '([':
            stack.append(char)
        
        # 닫힌 괄호인 경우
        elif char in ')]':
            # 스택이 비어있으면 매칭할 열린 괄호가 없음
            if not stack:
                return False
            
            # 스택에서 꺼낸 괄호가 현재 닫힌 괄호와 짝이 맞는지 확인
            if stack.pop() != pairs[char]:
                return False
    
    # 모든 괄호가 처리된 후 스택이 비어있어야 균형잡힘
    return len(stack) == 0

# 메인 실행 부분
while True:
    line = input()
    
    # 종료 조건: 온점 하나만 입력된 경우
    if line == '.':
        break
    
    # 문자열 끝의 온점 제거
    text = line.rstrip('.')
    
    # 균형 확인 후 결과 출력
    if is_balanced(text):
        print("yes")
    else:
        print("no")
