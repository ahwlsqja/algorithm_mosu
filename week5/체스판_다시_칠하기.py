n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

min_count = 64

for i in range(n-7):
    for j in range(m-7):
        count1 = 0
        for x in range(8):
            for y in range(8):
                if (x+y) % 2 == 0:
                    if board[i+x][j+y] != 'W':
                        count1 += 1
                else:
                    if board[i+x][j+y] != 'B':
                        count1 += 1
        count2 = 0
        for x in range(8):
            for y in range(8):
                if (x+y) % 2 == 0:
                    if board[i+x][j+y] != 'B':
                        count2+=1

                else:
                    if board[i+x][j+y] != 'W':
                        count2 += 1
        min_count = min(min_count, count1, count2)
print(min_count)

                
