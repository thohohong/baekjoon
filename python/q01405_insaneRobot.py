import sys

def recursion(level, x, y, cur_percent) :
    if board[y][x] == True :
        return 0

    if level == N :
        return cur_percent

    board[y][x] = True

    sum = 0
    for i in range(4) :
        if percent[i] != 0 :
            sum += recursion(level + 1, x + dir[i][1], y + dir[i][0], cur_percent * percent[i])
    
    board[y][x] = False
    return sum

dir = ((1, 0), (-1, 0), (0, 1), (0, -1)) # E W S N

input = sys.stdin.readline

percent = [0 for i in range(4)]

N, percent[0], percent[1], percent[2], percent[3] = map(int, input().split(" "))

for i in range(4) :
    percent[i] /= 100

board = [[False for i in range(N*2+1)] for j in range(N*2+1)]

answer = recursion(0, N, N, 1)

print(answer)