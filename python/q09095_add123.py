testCaseNum = int(input())

for testCase in range(0, testCaseNum) :
    n = int(input())

    dp = []
    for i in range(0, n + 3) :
        dp.insert(0, 0)
    dp[0] = 1
    for i in range(0, n) :
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
        dp[i + 3] += dp[i] 

    print(dp[n])