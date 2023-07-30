import sys
input = sys.stdin.readline

T = int(input())


for t in range(T) :
    K = int(input())
    pageNums = list(map(int, input().split(" ")))
    dp = [[0 for i in range(K)] for j in range(K)]
    # dp[i][j] is minimum cost to combine i to j
    
    # # initialize
    # for i in range(K) :
    #     dp[i][i] = pageNums[i]

    for diff in range(1, K) :
        for i in range(K-diff) :
            dp[i][i+diff] = 1e9
            curPageNum = pageNums[i+diff]
            for mid in range(i, i+diff) :
                curPageNum += pageNums[mid]
                dp[i][i+diff] = min(dp[i][i+diff], dp[i][mid]+dp[mid+1][i+diff]) 
            dp[i][i+diff] += curPageNum
    print(dp[0][K-1])