import sys
input = sys.stdin.readline

# cur부터 시작해 END까지 도달하는 데까지 필요한 비용을 반환.
def TSP(cur, visit) :
  if dp[cur][visit] != -1 :
    return dp[cur][visit]
  
  if visit == END :
    if cost[cur][0] != 0 :
      return cost[cur][0]
    else :
      return INF
  
  dp[cur][visit] = INF
  for i in range(1, N) :
    # 경로가 없음
    if cost[cur][i] == 0 :
      continue

    # 이미 방문함
    if visit & (1 << i):
      continue
    
    dp[cur][visit] = min(dp[cur][visit], cost[cur][i] + TSP(i, visit | 1 << i))
  
  return dp[cur][visit] # 최소 비용


N = int(input())

INF = 1e9
width = 1 << N
END = (1 << N) - 1

cost = []
for i in range(N) :
  cost.append(list(map(int, input().split(" "))))

dp = [[-1] * width for i in range(N)]

answer = TSP(0, 1)

print(answer)