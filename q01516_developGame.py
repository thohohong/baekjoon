import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
buildTime = [-1]
priority = [[]]

for t in range(N) :
    input_ = deque(map(int, input().split(" ")))
    input_.pop()
    buildTime.append(input_.popleft())
    priority.append(input_)

dp = [-1 for i in range(N+1)]

def DFS(node) :
    if dp[node] != -1 :
        return dp[node]

    maxTime = 0
    for next in priority[node] :
        maxTime = max(maxTime, DFS(next))
    
    maxTime += buildTime[node]
    dp[node] = maxTime
    return maxTime


for i in range(1, N+1) :
    print(DFS(i))

