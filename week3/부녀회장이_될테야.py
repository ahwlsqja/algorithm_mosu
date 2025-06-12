import sys

input = lambda: sys.stdin.readline().strip()
T = int(input())

room = [[0]*15 for _ in range(15)] #2차원 배열
for i in range(15):
    room[0][i] = i

for k in range(1, 15):
    for n in range(1, 15):
        room[k][n] = room[k-1][n] + room[k][n-1]

for i in range(T):
    k = int(input()) #1
    n = int(input()) #3  
    
    print(room[k][n])

