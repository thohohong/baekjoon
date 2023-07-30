import heapq
import sys

input = sys.stdin.readline
N, K = map(int, input().split(" "))

jewel = []
bag = []


for i in range(N) :
  M, V = map(int, input().split(" "))
  heapq.heappush(jewel, (M, V))

for j in range(K) :
  heapq.heappush(bag, int(input()))

sum = 0

tmpJewel = []
while bag :
  curBag = heapq.heappop(bag)
  while jewel and jewel[0][0] <= curBag :
    heapq.heappush(tmpJewel, -heapq.heappop(jewel)[1])
  
  if tmpJewel :
    sum += -heapq.heappop(tmpJewel)
  elif not jewel :
    break

print(sum)