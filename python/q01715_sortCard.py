import heapq
import sys

input = sys.stdin.readline

N = int(input())

pq = []

for i in range(N) :
    heapq.heappush(pq, int(input()))

answer = 0
while len(pq) >= 2 :
    first = heapq.heappop(pq)
    second = heapq.heappop(pq)
    answer += first
    answer += second
    heapq.heappush(pq, first + second)

print(answer)