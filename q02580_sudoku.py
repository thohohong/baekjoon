import sys
import copy

def printBoard(board, value) :
    global blank

    for y in range(9):
        for x in range(9):
            if board[y][x] == 0 :
                print(value[blank.index((y, x))], end="")
            else :
                print(board[y][x], end="")
            if x != 8 :
                print(" ", end="")
        print("")

def findCompleteBoard(idx, value) :
    isEnd = False
    if idx == len(value) :
        printBoard(board, value)
        return True

    y, x = blank[idx]
    areaIdx = int(y/3)*3+int(x/3)
    candidate = [a for a in missingNumRow[y] if a in missingNumCol[x] and a in missingNumArea[areaIdx]]
    if len(candidate) == 0 :
        return False

    for i in candidate :
        value[idx] = i
        missingNumRow[y].remove(i)
        missingNumCol[x].remove(i)
        missingNumArea[areaIdx].remove(i)
        isEnd = findCompleteBoard(idx + 1, value)
        if isEnd :
            return True
        missingNumRow[y].append(i)
        missingNumCol[x].append(i)
        missingNumArea[areaIdx].append(i)
    
    return False


input = sys.stdin.readline

board = [[] for i in range(9)]
blank = []

missingNumRow = [[] for i in range(9)]
missingNumCol = [[j for j in range(1, 10)] for i in range(9)]
missingNumArea = [[j for j in range(1, 10)] for i in range(9)]

# Get Input
for i in range(9) :
    board[i] = list(map(int, input().split(" ")))
    
    for j in range(9) :
        if board[i][j] == 0 :
            blank.append((i, j))

# Find missing num in every row, col, area
for i in range(9) :
    missingNumRow[i] = [a for a in range(1, 10) if a not in board[i]] # Row
    
    for j in range(9) : # Area
        idx = int(i/3)*3+int(j/3)
        if board[i][j] != 0 and board[i][j] in missingNumArea[idx] :
            missingNumArea[idx].remove(board[i][j])

    for j in range(9) : # Col
        if board[i][j] != 0 and board[i][j] in missingNumCol[j] :
            missingNumCol[j].remove(board[i][j])


value = [0 for i in range(len(blank))]
findCompleteBoard(0, value)