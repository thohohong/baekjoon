import sys

input = sys.stdin.readline

W, H = map(int, input().split(" "))
X, Y = map(int, input().split(" "))

HtoR = (Y, X) # Home to Restaurant
RtoS = (H-Y+1, W-X+1) # Restaurant to School

def countWayNUm(size) :
  dp = [[0 for j in range(size[1])] for i in range(size[0])]
  dp[0][0] = 1

  for i in range(size[0]) :
    for j in range(size[1]) :
      if i + 1 < size[0] :
        dp[i+1][j] += dp[i][j]
      if j + 1 < size[1] :
        dp[i][j+1] += dp[i][j]
  
  return dp[size[0]-1][size[1]-1]

wayToR = countWayNUm(HtoR)
wayToS = countWayNUm(RtoS) 

print((wayToR * wayToS) % 1000007) 