'''
&비트연산자와 and 논리 연산자를 헷갈리지 말자. 
while문의 조건 안이 True이면 반복되는 것이다. 자꾸 빠져나올 조건으로 착각해서 적지 말자.
'''
A, B = map(int, input().split())
    
while(A != 0 and B != 0):
    print(A + B)
    A, B = map(int, input().split())
    