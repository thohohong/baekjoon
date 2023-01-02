import sys
from collections import deque
import heapq


def dijkstra(start, target) :
  distance = [sys.maxsize for i in range(N)]
  distance[start] = 0
  q = []
  heapq.heappush(q, (start, 0))
  while len(q) > 0 :
    cur = heapq.heappop(q)

    if distance[cur[0]] < cur[1] :
      continue

    cost = distance[cur[0]] + 1
    for next in metro[cur[0]] :
      if cost < distance[next] :
        distance[next] = cost
        heapq.heappush(q, (next, cost))

  minimum = sys.maxsize
  for e in target :
    minimum = min(minimum, distance[e])

  return minimum

input = sys.stdin.readline

N = int(input())
metro = [set() for i in range(N)]
station = dict()

for lineNum in range(N) :
  cur_line = deque(map(int, input().split(" ")))
  cur_line.popleft()

  for e in cur_line :
    if e not in station :
      station[e] = set()
    if lineNum not in station[e] : # duplicate check
      for lineNum2 in station[e] :
        metro[lineNum2].add(lineNum)
        metro[lineNum].add(lineNum2)
    station[e].add(lineNum)
  
target = station[int(input())]

minTransferNum = sys.maxsize

for e in station[0] :
  result = dijkstra(e, target)
  minTransferNum = min(minTransferNum, result)

if minTransferNum == sys.maxsize :
  minTransferNum = -1
print(minTransferNum)