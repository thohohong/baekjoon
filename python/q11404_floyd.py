import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

minFee = [[INF for j in range(N + 1)] for i in range(N + 1)]

for i in range(1, N+1) :
    minFee[i][i] = 0

for i in range(M) :
    start, end, fee = map(int, input().split(" "))
    minFee[start][end] = fee if fee < minFee[start][end] else minFee[start][end]

for a in range(1, N+1) :
    for start in range(1, N+1) :
        for end in range(1, N+1) :
            minFee[start][end] = min(minFee[start][end], minFee[start][a] + minFee[a][end])

for a in range(1, N + 1) :
    for b in range(1, N + 1) :
        if(minFee[a][b] == INF) :
            print(0, end="")
        else :
            print(minFee[a][b], end="")
        if b != N :
            print(" ", end="")
    print("")