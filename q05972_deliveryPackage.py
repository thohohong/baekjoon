import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split(" "))

road = [[] for i in range(N+1)]
for i in range(M) :
  A, B, C = map(int, input().split(" "))
  road[A].append((B, C))
  road[B].append((A, C))

queue = []
dp = [1e9 for i in range(N+1)]
dp[1] = 0

heapq.heappush(queue, (1, 0))

while queue :
  cur = heapq.heappop(queue)

  if cur[1] > dp[cur[0]] :
    continue

  for e in road[cur[0]] :
    if cur[1] + e[1] < dp[e[0]] :
      dp[e[0]] = cur[1] + e[1]
      heapq.heappush(queue, (e[0], dp[e[0]]))

print(dp[N])