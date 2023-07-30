import sys
from collections import deque

dirType = [(0, -1), (-1, 0), (0, 1), (1, 0)] # L U R D
input = sys.stdin.readline

N = int(input()) # size of board
appleNum = int(input()) # number of apples


### Set board
board = [[-1 for col in range(N+2)] for row in range(N+2)] # -1 : empty, 0 : apple, 1 : snake

for i in range(N+2) :
    board[i][0] = 1
    board[i][N+1] = 1
    if i == 0 or i == N + 1 :
        for j in range(N+2) :
            board[i][j] = 1

for i in range(appleNum) :
    row, col = map(int, input().split(" "))
    board[row][col] = 0
board[1][1] = 1
dir = 2

### Set Queue
snake = deque()
x, y = 1, 1
snake.append((y, x))

### Get command
cmd = deque()
L = int(input()) # number of rotating
for i in range(L) :
    X, DIR = input().split(" ")
    X = int(X)
    cmd.append((X, DIR))

### Play Game
time = 0
while True :
    if len(cmd) != 0 and cmd[0][0] == time :
        CMD = cmd.popleft()
        if CMD[1][0] == 'L' :
            dir = (dir - 1) % 4
        elif CMD[1][0] == 'D' :
            dir = (dir + 1) % 4
    
    cur = snake[0]
    new = (dirType[dir][0] + cur[0], dirType[dir][1] + cur[1])

    if board[new[0]][new[1]] == 1 : # GameOver
        break
    elif board[new[0]][new[1]] == 0 : # Eat Apple
        snake.appendleft(new)
    else :
        pre = snake.pop()
        board[pre[0]][pre[1]] = -1
        snake.appendleft(new)

    board[new[0]][new[1]] = 1
    time += 1

time += 1
print(time)
