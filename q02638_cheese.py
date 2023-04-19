import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(1e5))

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split(" "))
plate = []
for i in range(N) :
    plate.append(list(map(int, input().split(" "))))

def DFS(i, j) :
    plate[i][j] = 2
    for dy, dx in DIR :
        if i+dy >= 0 and i+dy < N and j+dx >= 0 and j+dx < M and plate[i+dy][j+dx] == 0 :
            DFS(i+dy, j+dx)

t = 0
while True :
    DFS(0, 0)

    disappear = []
    for i in range(N) :
        for j in range(M) :
            if plate[i][j] == 1 :
                count = 0
                for dy, dx in DIR :
                    if plate[i+dy][j+dx] == 2 :
                        count += 1
                if count >= 2 :
                    disappear.append((i, j))

    for i, j in disappear :
        plate[i][j] = 0
    t += 1

    for i in range(N) :
        for j in range(M) :
            if plate[i][j] == 2 :
                plate[i][j] = 0

    sumCheese = 0
    for i in range(N) :
        sumCheese += plate[i].count(1)
    if sumCheese == 0 :
        break

print(t)
