import sys
input = sys.stdin.readline

N = int(input())
lineList = []

for i in range(N) :
    A, B = map(int, input().split(" "))
    lineList.append((A, B))

lineList.sort()

dp = [1 for i in range(N)]
for i in range(N) :
    for j in range(i) :
        if lineList[i][1] >= lineList[j][1] :
            dp[i] = max(dp[i], dp[j] + 1)

result = N - max(dp)
print(result)