import heapq
import sys

dir = ((0, -1), (-1, 0), (0, 1), (1, 0))
count = 1
while True :
    N = int(input(""))

    if N == 0 :
        break

    cave = [[0 for column in range(N)] for row in range(N)]
    dp = [[sys.maxsize for column in range(N)] for row in range(N)]

    # Get Input
    for row in range(N) :
        rowInput = input("").split(" ")
        for col in range(N) :
            cave[row][col] = int(rowInput[col])
    
    q = []
    dp[0][0] = cave[0][0]
    heapq.heappush(q, (dp[0][0], 0, 0))

    while not len(q) == 0 :
        cur = heapq.heappop(q)

        if cur[0] > dp[cur[1]][cur[2]] :
            continue

        for d in dir : 
            newX = cur[2] + d[1]
            newY = cur[1] + d[0]

            if newX >= 0 and newX < N and newY >= 0 and newY < N :
                cost = cur[0] + cave[newY][newX]
                if cost < dp[newY][newX] :
                    dp[newY][newX] = cost
                    heapq.heappush(q, (cost, newY, newX))


    print("Problem %d: %d" % (count, dp[N-1][N-1]))
    count += 1

    