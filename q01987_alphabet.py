import sys

dir = ((-1, 0), (0, -1), (1, 0), (0, 1))

# curNum : the number of spaces that have passed so far
def DFS(x, y, curNum, R, C) :
    if x < 0 or x >= C or y < 0 or y >= R :
        return -1
    if check[ord(board[y][x]) - ord('A')] :
        return -1
    if boardVisit[y][x] :
        return -1
    
    check[ord(board[y][x]) - ord('A')]= True
    boardVisit[y][x] = True

    maxNum = curNum
    for nextDir in dir :
        num = DFS(x + nextDir[0], y + nextDir[1], curNum + 1, R, C)
        maxNum = max(maxNum, num)

    check[ord(board[y][x]) - ord('A')] = False
    boardVisit[y][x] = False
    
    return maxNum



input = sys.stdin.readline
R, C = map(int, input().split(" "))
board = []

boardVisit = [[False for i in range(C)] for j in range(R)]
check = [False for i in range(26)]

for i in range(R) :
    board.append(list(input().strip()))


maxNum = DFS(0, 0, 1, R, C)
print(maxNum)