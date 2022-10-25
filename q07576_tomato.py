from collections import deque

dir = ((-1, 0), (0, -1), (1, 0), (0, 1))
userInput = input("").split(" ")

M = int(userInput[0])
N = int(userInput[1])

box = [[0 for col in range(M)] for row in range(N)]
q = deque()
freshTomato = 0

# get input
for row in range(N) :
    userInput = input("").split(" ")
    for col in range(M) :
        box[row][col] = int(userInput[col])
        if box[row][col] == 1 :
            q.append((row, col, 0))
        elif box[row][col] == 0 :
            freshTomato += 1

depth = 0

while not len(q) == 0 :
    cur = q.popleft()

    for d in dir :
        x = cur[1] + d[1]
        y = cur[0] + d[0]
        if x >= 0 and x < M and y >= 0 and y < N and box[y][x] == 0 :
            box[y][x] = 1
            freshTomato -= 1
            q.append((y, x, cur[2] + 1))
            if cur[2] + 1 > depth :
                depth = cur[2] + 1

if freshTomato > 0 :
    print(-1)
else :
    print(depth)