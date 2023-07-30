import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split(" "))
graph = [[] for i in range(V+1)]
dp = [1e9 for i in range(V+1)]

start = int(input())
for i in range(E) :
    u, v, w = map(int, input().split(" "))
    graph[u].append((v, w))

def dijkstra(node) :
    pq = []
    heapq.heappush(pq, (0, start))
    dp[start] = 0

    while pq :
        distance, cur = heapq.heappop(pq)
        if dp[cur] < distance : # 가는 길보다 현재까지가 더 짧음
            continue
        for v, w in graph[cur] :
            if distance + w < dp[v] :
                dp[v] = distance + w
                heapq.heappush(pq, (dp[v], v))

dijkstra(start)
for i in range(1, V+1) :
    if dp[i] == 1e9 :
        print("INF")
    else :
        print(dp[i])