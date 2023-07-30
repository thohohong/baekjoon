import sys
input = sys.stdin.readline

T = int(input())

dp = [[-1 for j in range(10)] for i in range(65)]

results = [-1 for i in range(65)]
results[1] = 10

def DFS(n, i) :
    if n == 1 :
        return i+1
    
    if dp[n][i] != -1 :
        return dp[n][i]

    result = 0
    for next in range(i+1) :
        result += DFS(n-1, next)
    
    dp[n][i] = result
    return result

for _ in range(T) :
    N = int(input())
    result = 0
    
    if results[N] != -1 :
        print(results[N])
        continue

    for i in range(10) :
        result += DFS(N-1, i)
    
    results[N] = result
    print(result)