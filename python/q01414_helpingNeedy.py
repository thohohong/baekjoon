import sys
import heapq
input = sys.stdin.readline

N = int(input())
lines = [[0 for i in range(N)] for j in range(N)]
check = [False for i in range(N)]
q = []

lengthSum = 0
for i in range(N):
  cur = list(map(ord, input().strip()))
  for j in range(N):
    if cur[j] == ord('0') :
      lines[i][j] = 0     
    elif cur[j] >= ord('A') and cur[j] <= ord('Z') :
      lines[i][j] = cur[j] - ord('A') + 27
    else :
      lines[i][j] = cur[j] - ord('a') + 1
  lengthSum += sum(lines[i])

minLength = 0
heapq.heappush(q, (0, 0)) # (cost, nextNode)

while q :
  cost, curNode = heapq.heappop(q)
  if check[curNode] == True :
    continue

  check[curNode] = True
  minLength += cost

  for nextNode in range(N) :
    if check[nextNode] == True :
      continue
    if lines[curNode][nextNode] != 0 and lines[nextNode][curNode] != 0 :
      nextCost = min(lines[curNode][nextNode], lines[nextNode][curNode])
    elif lines[curNode][nextNode] == 0 and lines[nextNode][curNode] == 0:
      continue
    elif lines[curNode][nextNode] == 0 :
      nextCost = lines[nextNode][curNode]
    elif lines[nextNode][curNode] == 0 :
      nextCost = lines[curNode][nextNode]
    
    heapq.heappush(q, (nextCost, nextNode))

for isChecked in check :
  if not isChecked :
    print(-1)
    exit(0)
print(lengthSum - minLength)