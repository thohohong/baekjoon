import sys
N = int(input(""))

maze = [0 for i in range(N)]
dp = [sys.maxsize for i in range(N)]
dp[0] = 0

maze_input = input("").split(" ")

for i in range(N) :
    maze[i] = int(maze_input[i])

for i in range(N) :
    for j in range(maze[i] + 1) :
        if (i + j < N) :
            dp[i+j] = min(dp[i] + 1, dp[i+j])
        else :
            dp[N-1] = min(dp[i] + 1, dp[N-1])

if dp[N-1] == sys.maxsize :
    print(-1, end="")
else :
    print(dp[N-1], end="")