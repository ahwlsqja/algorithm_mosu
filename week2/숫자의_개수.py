'''
- 실제로 반복문을 이중으로 써도 (0-9까지의 for문)x(AxBxC의 결과 자리들의 수) 만큼 루프를 도렉 된다.
- 문자열과 정수형 자료형을 정확히 구분하여 부등호를 사용해야함.
'''
A =int(input())
B = int(input())
C = int(input())
S = str(A * B* C)
for i in range(10):
    count = 0
    for j in range(len(S)):
        if(S[j] == str(i)):
            count += 1
    print(count)
