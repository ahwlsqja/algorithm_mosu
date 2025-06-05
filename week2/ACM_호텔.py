'''
테스트케이스를 추가로 만들어서 해볼것. 
예외 케이스를 고려하여 코드를 짜주어야함. 
딱 나누어 떨어질때 -> 나머지가 0일때가 특이케이스가 될 수 있지 않을까? 고려해야함.
'''
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor == 0:
        floor = H
        room = int(N//H)
    else: 
        room = int(N//H) + 1
    if len(str(room)) == 1:
        room = "0"+ str(room)
    print(floor, end='')
    print(room, end='')
    print()