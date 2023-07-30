import sys
import heapq

N = int(input(""))
M = int(input(""))

info = [[] for i in range(N+1)]

for i in range(M) :
    userInput = input("").split(" ")

    start = int(userInput[0])
    end = int(userInput[1])
    cost = int(userInput[2])

    info[start].append((end, cost))

userInput = input("").split(" ")

start = int(userInput[0])
end = int(userInput[1])

q = []

dp = [sys.maxsize for i in range(N + 1)]
dp[start] = 0
heapq.heappush(q, (start, 0))

while not len(q) == 0 :
    cur = heapq.heappop(q)
    
    if cur[1] > dp[cur[0]] :
        continue

    for dir in info[cur[0]] :
        cost = dir[1] + cur[1]
        if cost < dp[dir[0]] :
            dp[dir[0]] = cost
            heapq.heappush(q, (dir[0], cost))

print(dp[end])