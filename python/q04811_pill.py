import sys
input = sys.stdin.readline
dp = [[-1 for i in range(31)] for j in range(31)]

def DFS(w, h) :
    if w == 0 and h == 0 :
        return 1
    if dp[w][h] != -1 :
        return dp[w][h]

    result = 0
    if w > 0 :
        result += DFS(w-1, h+1)
    if h > 0 :
        result += DFS(w, h-1)
    
    dp[w][h] = result
    return result

while True :
    N = int(input())
    if N == 0 :
        break

    if dp[N][0] != -1 :
        print(dp[N][0])
        continue

    DFS(N, 0)
    print(dp[N][0])
    