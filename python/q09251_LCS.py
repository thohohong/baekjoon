first = input().strip()
second = input().strip()

dp = [[0 for i in range(len(second))] for j in range(len(first))]

# dp[i][j]는 first의 0~i까지, second의 0~j까지의 문자열에서의 LCS

maxValue = 0
for i in range(len(first)) :
    for j in range(len(second)) :
        if first[i] == second[j] :
            if i >= 1 and j >= 1 :
                dp[i][j] = dp[i-1][j-1] + 1
            else :
                dp[i][j] = 1
        else :
            up, left = 0, 0
            if i >= 1 :
                up = dp[i-1][j]
            if j >= 1 :
                left = dp[i][j-1]
            dp[i][j] = max(up, left)
        maxValue = max(maxValue, dp[i][j])

print(maxValue)