import sys
input = sys.stdin.readline
INF = 1e9

def DFS(node) :
    if dp[node] != -1 :
        return dp[node]
    
    costSum = 0
    check[node] = True

    for i in connection[node] :
        v, w = i[0], i[1]
        if not check[v] :
            costSum += min(DFS(v), w)
    
    if costSum == 0 :
        costSum = INF
    dp[node] = costSum
    return costSum

while True :
    try :
        N, C = map(int, input().split(" "))

        connection = [[] for i in range(N+1)]
        dp = [-1 for i in range(N+1)]
        check = [False for i in range(N+1)]

        for i in range(N-1) :
            u, v, w = map(int, input().split(" "))
            connection[u].append((v, w))
            connection[v].append((u, w))

        print(DFS(C))

    except :
        break