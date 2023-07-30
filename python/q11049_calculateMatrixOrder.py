import sys
input = sys.stdin.readline
INF = 1e9
N = int(input())
matrix = []

# dp[i][j] is number of calculation from ith to jth
dp = [[-1 for i in range(N)] for j in range(N)]

for i in range(N):
  matrix.append(list(map(int, input().split(" "))))
  dp[i][i] = 0

for diff in range(1, N) :
  for left in range(N) :
    right = left + diff
    # out of range
    if right >= N :
      break
    
    dp[left][right] = INF
    for mid in range(left, right) :
      curCalculation = matrix[left][0] * matrix[right][1] * matrix[mid][1]  
      dp[left][right] = min(dp[left][right], dp[left][mid] + dp[mid+1][right] + curCalculation)

print(dp[0][N-1])