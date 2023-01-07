import sys

input = sys.stdin.readline

# Get Input
N = int(input())
stair = []
for i in range(N) :
  stair.append(int(input()))

dp = [[0 for i in range(N)] for j in range(2)]

# initialize
dp[0][0] = stair[0]
dp[1][0] = stair[0]

if N > 1 :
  dp[0][1] = stair[1]

for i in range(N-1) :
  dp[1][i+1] = max(dp[1][i+1], dp[0][i] + stair[i+1])
  if i < N-2 :
    dp[0][i+2] = max(dp[0][i+2], dp[0][i] + stair[i+2], dp[1][i] + stair[i+2])

print(max(dp[0][N-1], dp[1][N-1]))
