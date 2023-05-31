N = int(input())

if N % 2 == 1 :
    print(0)
    exit(0)

# n칸을 채우는 경우의 수
dp = [0 for i in range(N+1)]
dp[0] = 1
# dp[2] = 3
# dp[4] = 11

def DFS(n) :
    if dp[n] != 0 :
        return dp[n]
    
    result = 0
    result += 3 * DFS(n-2)
    
    i = 4
    while i <= n :
        result += 2 * DFS(n-i)
        i += 2

    dp[n] = result
    return result

result = DFS(N)
print(result)