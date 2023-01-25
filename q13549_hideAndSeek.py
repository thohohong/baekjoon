import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9

queue = deque()

N, K = map(int, input().split(" "))
queue.appendleft(N)
dp = [INF for i in range(200000)]
dp[N] = 0

while queue :
  cur = queue.popleft()

  if cur-1 >= 0 and dp[cur-1] > dp[cur] + 1 :
    dp[cur-1] = dp[cur] + 1
    queue.append(cur-1)
  if cur+1 < 200000 and dp[cur+1] > dp[cur] + 1 :
    dp[cur+1] = dp[cur] + 1
    queue.append(cur+1)
  if cur*2 < 200000 and dp[cur*2] > dp[cur] :
    dp[cur*2] = dp[cur]
    queue.appendleft(cur*2)

print(dp[K])