import sys
input = sys.stdin.readline

nextDIR = ((1, 0), (0, 1), (1, 1))

N, M = map(int, input().split(" "))
maze = []
for i in range(N) :
    maze.append(list(map(int, input().split(" "))))

dp = [[0 for i in range(M)] for j in range(N)]
dp[0][0] = maze[0][0]

for r in range(N) :
    for c in range(M) :
        for dy, dx in nextDIR :
            if r + dy >= 0 and r + dy < N and c + dx >= 0 and c + dx < M :
                dp[r+dy][c+dx] = max(dp[r+dy][c+dx], dp[r][c] + maze[r+dy][c+dx])

print(dp[N-1][M-1])