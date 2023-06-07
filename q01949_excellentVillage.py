import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
population = [0] + list(map(int, input().split(" ")))

adjacency = [[] for i in range(N+1)]

for i in range(N-1) :
    A, B = map(int, input().split(" "))
    adjacency[A].append(B)
    adjacency[B].append(A)

dp = [[-1 for i in range(2)] for j in range(N+1)]

def delParent(node) :
    for next in adjacency[node] :
        idx = adjacency[next].index(node)
        del adjacency[next][idx]
        delParent(next)

EXCELLENT = 1
NOT_EXCELLENT = 0

def DFS(node) :
    dp[node][EXCELLENT] = population[node]
    dp[node][NOT_EXCELLENT] = 0

    for next in adjacency[node] :
        DFS(next)
        dp[node][EXCELLENT] += dp[next][NOT_EXCELLENT]
        dp[node][NOT_EXCELLENT] += max(dp[next][EXCELLENT], dp[next][NOT_EXCELLENT])

delParent(1)
DFS(1)
print(max(dp[1][EXCELLENT], dp[1][NOT_EXCELLENT]))