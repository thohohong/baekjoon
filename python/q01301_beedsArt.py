import sys

input = sys.stdin.readline

# Get input
N = int(input())

beedsNum = [0 for i in range(5)]
for i in range(N) :
  beedsNum[i] = int(input())
totalNum = sum(beedsNum)

def addBeeds(cur, pre2, pre1) :
  if cur >= totalNum :
    return 1

  if dp[beedsNum[0]][beedsNum[1]][beedsNum[2]][beedsNum[3]][beedsNum[4]][pre2][pre1] != -1 :
    return dp[beedsNum[0]][beedsNum[1]][beedsNum[2]][beedsNum[3]][beedsNum[4]][pre2][pre1]

  sum = 0  
  for i in range(N) :
    if i != pre1 and i != pre2 and beedsNum[i] > 0:
      beedsNum[i] -= 1
      sum += addBeeds(cur + 1, pre1, i)
      beedsNum[i] += 1

  dp[beedsNum[0]][beedsNum[1]][beedsNum[2]][beedsNum[3]][beedsNum[4]][pre2][pre1] = sum
  return sum

dp = [[[[[[[-1 for i in range(N + 1)] for j in range(N + 1)] for e in range(11)] for d in range(11)] for c in range(11)] for b in range(11)] for a in range(11)]
print(addBeeds(0, -1, -1))