import sys

input = sys.stdin.readline

def makePelindrome(str) :
  dp = [[MAX_SIZE for i in range(0, length)] for j in range(0, length)]

  mid = length // 2
  
  dp[0][0] = 0
  dp[length-1][length-1] = 0

  for i in range(1, length-1) :
    dp[i][i] = 0
    
    if str[i] == str[i+1] :
      dp[i][i+1] = 0
    else :
      dp[i][i+1] = 1
    
    if str[i-1] == str[i] :
      dp[i-1][i] = 0
    else :
      dp[i-1][i] = 1
  
  for i in reversed(range(0, length)) :
    for j in range(0, length) :
      if i > j :
        continue
      if i-1 >= 0 :
        dp[i-1][j] = min(dp[i-1][j], dp[i][j] + 1)
      if j+1 < length :
        dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
      if i-1 >= 0 and j+1 < length :
        if str[i-1] == str[j+1] :
          dp[i-1][j+1] = min(dp[i-1][j+1], dp[i][j]) 
        else :
          dp[i-1][j+1] = min(dp[i-1][j+1], dp[i][j] + 1)
  
  return dp[0][length-1]

MAX_SIZE = 100
org = list(input().strip())
length = len(org)
minValue = makePelindrome(org)
for i in range(length) :
  for j in range(length) :
    if org[i] == org[j] :
      continue
    org[i], org[j] = org[j], org[i]
    minValue = min(minValue, makePelindrome(org) + 1)
    org[i], org[j] = org[j], org[i]

print(minValue)