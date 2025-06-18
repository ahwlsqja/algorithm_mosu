from collections import deque
queue = deque()

N, K = map(int, input().split())
for i in range(1, N+1):
    queue.append(i)
print("<", end="")
answer = []
while(queue):
    for i in range(K):
        if i == K-1:
            answer.append(queue.popleft())
            break
        queue.append(queue.popleft())
for i in range(len(answer)):
    if i == len(answer) - 1:
        print(answer[i], end="")
    else:
        print(answer[i], end=", ")
print(">", end="")


