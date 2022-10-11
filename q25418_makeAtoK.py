import sys

userInput = input("")
a = int(userInput.split(" ")[0])
k = int(userInput.split(" ")[1])

# dp[i] is minimum number of calculation to make i
dp = list(sys.maxsize for i in range(k+1))
dp[a] = 0

for i in range(a, k):
    dp[i + 1] = min(dp[i+1], dp[i] + 1)
    if i * 2 <= k :
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)

print(dp[k])
