import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

time = [-1]
priority = [-1]
completed = [False for i in range(N+1)]

endTime = [-1 for i in range(N+1)]

for i in range(N) :
    data = list(map(int, input().split(" ")))
    time.append(data[0])
    priority.append(data[2:])

for i in range(1, N+1) :
    if priority[i] :
        maxTime = 0
        for p in priority[i] :
            maxTime = max(maxTime, endTime[p])
        endTime[i] = maxTime + time[i]
    else :
        endTime[i] = time[i]

print(max(endTime))