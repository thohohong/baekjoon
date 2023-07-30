import sys
input = sys.stdin.readline

N = int(input())
supervisor = list(map(int, input().split(" ")))
tree = [[] for i in range(N)]
dp = [0 for i in range(N)]

for i in range(1, N) :
  tree[supervisor[i]].append(i)

for i in reversed(range(N)) :
  if not tree[i] : # no sub
    continue
  
  subCountList = []

  for next in tree[i] :
    curSum = dp[next]
    subCountList.append(curSum)

  subCountList.sort(reverse=True)
  
  for j in range(len(subCountList)) :
    dp[i] = max(dp[i], subCountList[j] + j)

  dp[i] += 1
  
print(dp[0])