import sys
from collections import deque

def printBoard(board) :
    global blank

    for y in range(9):
        for x in range(9):
            print(board[y][x], end="")
            if x != 8 :
                print(" ", end="")
        print("")

def isValid(x, y, value) :
    for i in range(9) :
        if board[y][i] == value :
            return False
    
    for i in range(9) :
        if board[i][x] == value :
            return False
    
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3

    for i in range(start_y, start_y + 3) :
        for j in range(start_x, start_x + 3) :
            if board[i][j] == value :
                return False

    return True

def findCompleteBoard(blank, idx, value) :
    if idx == len(blank) :
        printBoard(board)
        return True
    
    y, x = blank[idx]
    if not isValid(x, y, value) :
        return False

    board[y][x] = value

    for i in range(1, 10) :
        if findCompleteBoard(blank, idx + 1, i) :
            return True
    board[y][x] = 0
    return False

input = sys.stdin.readline

board = [[] for i in range(9)]
blank = []

# Get Input
for i in range(9) :
    board[i] = list(map(int, input().split(" ")))
    
    for j in range(9) :
        if board[i][j] == 0 :
            blank.append((i, j))

for i in range(1, 10) :
    if findCompleteBoard(blank, 0, i) :
        break