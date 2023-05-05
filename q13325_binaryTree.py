import sys
input = sys.stdin.readline

k = int(input())
weight = list(map(int, input().split(" ")))
dp = [1e9 for i in range(pow(2, k+1))]

for i in range(pow(2, k) - 1, pow(2, k+1)) : 
    dp[i] = 0

result = 0
for i in reversed(range(pow(2, k)-1)) :
    cur = max(dp[i*2+1] + weight[i*2], dp[i*2+2] + weight[i*2+1])
    result += cur - dp[i*2+1] + cur - dp[i*2+2]
    dp[i] = cur

print(result)
