import sys
from collections import deque


input = sys.stdin.readline
DIR = ((0, -1), (-1, 0), (0, 1), (1, 0))
N, M = map(int, input().split(" "))

def minusToZero(field, zeroList) :
    for y, x in zeroList :
        field[y][x] = 0

def isSeparated(field, countIceberg) :
    # Find first coordinate which is not 0
    flag = False
    for i in range(N) :
        for j in range(M) :
            if field[i][j] != 0 :
                flag = True
                break
        if flag :
            break
    
    # BFS
    visit = [[False for j in range(M)] for i in range(N)]
    countCurLand = 0
    queue = deque()
    queue.append((i, j))
    visit[i][j] = True
    while queue :
        cur = queue.popleft()
        countCurLand += 1
        for dy, dx in DIR :
            y = cur[0] + dy
            x = cur[1] + dx
            if y >= 0 and y < N and x >= 0 and x < M :
                if not visit[y][x] and field[y][x] != 0 :
                    visit[y][x] = True
                    queue.append((y, x))

    # Check Condition
    if countIceberg != countCurLand :
        return True
    else :
        return False
    
field = []
for i in range(N) :
    field.append(list(map(int, input().split(" "))))

yearCount = 0
while True :
    yearCount += 1
    countIceberg = 0 # number of iceberg
    turnIntoZero = [] # list of Iceberg that turn into zero in this turn
    for i in range(N) :
        for j in range(M) :
            if field[i][j] != 0 :
                count0 = 0
                for dy, dx in DIR :
                    y = i + dy
                    x = j + dx
                    if y >= 0 and y < N and x >= 0 and x < M :
                        if field[y][x] == 0 :
                            count0 += 1
                field[i][j] -= count0
                if field[i][j] <= 0 :
                    field[i][j] = -1
                    turnIntoZero.append((i, j))
            if field[i][j] != 0 and field[i][j] != -1 :
                countIceberg += 1

    # Iceberg is all melted before icebergs are separated
    if countIceberg == 0 :
        print("0")
        exit(0)

    # Every Iceberg is not melted totally
    if not turnIntoZero :
        continue

    minusToZero(field, turnIntoZero)
    if isSeparated(field, countIceberg) :
        break

print(yearCount)