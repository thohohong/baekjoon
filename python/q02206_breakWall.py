import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))
field = []
for i in range(N) :
    field.append(list(map(int, input().strip())))

DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
visit = [[[False, False] for j in range(M)] for i in range(N)]

q = deque()
q.append((0, 0, 0, 1))
visit[0][0][0] = True
isEnd = False

while q :
    y, x, isBroken, distance = q.popleft()

    if y == N-1 and x == M-1 :
        isEnd = True
        print(distance)
        break
    for dy, dx in DIR :
        nextY = y+dy
        nextX = x+dx
        if not(nextY >= 0 and nextY < N and nextX >= 0 and nextX < M) :
            continue
        if field[nextY][nextX] == 0 and not visit[nextY][nextX][isBroken]:
            q.append((nextY, nextX, isBroken, distance+1))
            visit[nextY][nextX][isBroken] = True
        elif isBroken == 1 :
            continue
        elif not visit[nextY][nextX][1]:
            q.append((nextY, nextX, 1, distance+1))
            visit[nextY][nextX][1] = True

if not isEnd :
    print(-1)