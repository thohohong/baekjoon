import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
board = []
check = [[False for j in range(M)] for i in range(N)]
dp = [[0 for j in range(M)] for i in range(N)]

for i in range(N) :
    board.append(input().strip())

maxMove = 0
dir = ((-1, 0), (0, 1), (1, 0), (0, -1))

def DFS(x, y, moveNum) :
    global maxMove
    if x < 0 or x >= M or y < 0 or y >= N or board[y][x] == 'H' :
        return
    
    if dp[y][x] >= moveNum :
        return
    else :
        dp[y][x] = moveNum

    if check[y][x] :
        print(-1)
        exit(0)
    
    check[y][x] = True

    maxMove = max(maxMove, moveNum)
    curBoard = int(board[y][x])
    for _dir_ in dir :
        DFS(x + _dir_[1] * curBoard, y + _dir_[0] * curBoard, moveNum + 1)
    
    check[y][x] = False

DFS(0, 0, 1)

print(maxMove)