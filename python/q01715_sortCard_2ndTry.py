import sys
import heapq

input = sys.stdin.readline

N = int(input())
pq = []

for i in range(N) :
    heapq.heappush(pq, int(input()))

result = 0
while len(pq) > 1 :
    first = heapq.heappop(pq)
    second = heapq.heappop(pq)

    result += first + second
    heapq.heappush(pq, first+second)

print(result)