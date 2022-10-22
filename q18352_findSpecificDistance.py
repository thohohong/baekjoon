import sys
import heapq

# no. 18352
# Print out every node which has an minimum cost K
# using Djikstra Algorithm

userInput = input("").split(" ")
N, M, K, X = int(userInput[0]), int(userInput[1]), int(userInput[2]), int(userInput[3])

# N : number of city
# M : number of road
# K : minimum cost K
# X : the city to start at

graph = [[] for i in range(N+1)] # 인접 리스트
distance = [sys.maxsize for i in range(N+1)]

# get edge and make graph
for i in range(M) :
  userInput = input("").split(" ")
  graph[int(userInput[0])].append(int(userInput[1]))


q = [] # (A, B) : A is node, B is cost for visiting A by this route
heapq.heappush(q, (X, 0)) 
distance[X] = 0

while (not len(q) == 0) :
  cur = heapq.heappop(q)
  
  if distance[cur[0]] < cur[1] :
    continue

  cost = distance[cur[0]] + 1
  for next in graph[cur[0]] :
    if cost < distance[next] :
      distance[next] = cost
      heapq.heappush(q, (next, cost))

isPrinted = False


for i in range(N+1) :
  if K == distance[i] :
    print(i)
    isPrinted = True

if not isPrinted :
  print(-1)