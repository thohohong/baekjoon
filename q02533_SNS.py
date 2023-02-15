import sys
import copy
import heapq
from collections import deque

input = sys.stdin.readline
N = int(input())

tree = [[] for i in range(N+1)]

dp = [[-1 for i in range(N+1)] for j in range(2)]

for i in range(N-1) :
  A, B = map(int, input().split(" "))
  tree[A].append(B)
  tree[B].append(A)


def organizeTree(start) :
  global hq
  global maxDepth
  queue = deque()
  queue.append(start)
  
  stack.append((start, True))
  stack.append((start, False))

  while queue :
    cur = queue.popleft()
    
    check[cur] = True
    nextNodes = copy.deepcopy(tree[cur])
    for i in nextNodes :
      if check[i] :
        tree[cur].remove(i)
      else :
        queue.append(i)
        stack.append((i, True))
        stack.append((i, False))

def DFS() :
  while stack :
    node, isEA = stack.pop()

    EAidx = 0
    if isEA :
      EAidx = 1
    else :
      EAidx = 0

    if not tree[node] :
      if isEA :
        dp[EAidx][node] = 1
      else :
        dp[EAidx][node] = 0
      continue

    minSum = 0
    if isEA :
      for i in tree[node] :
        minSum += min(dp[1][i], dp[0][i])
      minSum += 1
    else :
      for i in tree[node] :
        minSum += dp[1][i]
    dp[EAidx][node] = minSum

check = [False for i in range(N+1)]
stack = []

organizeTree(1)
DFS()
print(min(dp[1][1], dp[0][1]))