import sys
from collections import deque

sys.setrecursionlimit(10**4)

N, M = map(int, input().split())

D = [0] + [int(input()) for i in range(N)]
C = [0] + [int(input()) for i in range(M)]

dp = [[-1 for i in range(N+1)] for j in range(M+1)]
# dp[day][city]

# 0번째 도시에서 움직이지 않을 때
for i in range(M+1) :
    dp[i][0] = 0

# 0일에 1 이상의 도시에 있을 수 없음
for i in range(1, N+1) :
    dp[0][i] = 1e9


def DFS(day, city) :
    if day < 0 or city < 0 :
        return 1e9

    if dp[day][city] != -1 :
        return dp[day][city]
    
    # didn't move
    result1 = DFS(day-1, city)

    # move
    result2 = DFS(day-1, city-1) + C[day] * D[city]

    dp[day][city] = min(result1, result2)
    return dp[day][city]

DFS(M, N)
print(dp[M][N])