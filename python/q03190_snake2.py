import sys
from collections import deque

input = sys.stdin.readline

BODY = 2
APPLE = 1
BLANK = 0
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

N = int(input())

# Init Board
board = [[BLANK for i in range(N)] for i in range(N)]
board[0][0] = BODY


# Get Apple
appleNum = int(input())
for i in range(appleNum) :
    row, col = map(int, input().split(" "))
    board[row-1][col-1] = APPLE

# Get Turn
turnNum = int(input())
turnInfo = deque()
for i in range(turnNum) :
    sec, dir = input().strip().split(" ")
    turnInfo.append((int(sec), dir))

sec = 0
dir = 0
snake = deque()
snake.append((0, 0))
curCoor = (0, 0)

while True :
    nextRow = curCoor[0] + DIR[dir][0]
    nextCol = curCoor[1] + DIR[dir][1]

    if nextRow < 0 or nextRow >= N or nextCol < 0 or nextCol >= N or board[nextRow][nextCol] == BODY :
        sec += 1
        break
    else :
        snake.append((nextRow, nextCol))
        if board[nextRow][nextCol] == BLANK :
            curRow, curCol = snake.popleft()
            board[curRow][curCol] = BLANK
        board[nextRow][nextCol] = BODY
    
    curCoor = (nextRow, nextCol)
    
    sec += 1
    if turnInfo and sec == turnInfo[0][0] :
        if turnInfo[0][1] == 'L' : # turn left
            dir = (dir - 1) % 4
        else :
            dir = (dir + 1) % 4 # turn right
        turnInfo.popleft()

print(sec)