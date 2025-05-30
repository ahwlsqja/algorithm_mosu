'''
테스트 케이스 개수가 주어지지 않았는데?
try, except 구문을 활용할 수 있다. 
이에 대해서 자세히 블로그에 기록할 필요가 있음
'''
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break