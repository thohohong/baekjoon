import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+1)
# N : number of nodes
# R : the number of roots
# Q : number of query
N, R, Q = map(int, input().split(" "))

tree = [[] for i in range(N+1)]
dp = [-1 for i in range(N+1)]
check = [False for i in range(N+1)]

for i in range(N-1) : 
  A, B = map(int, input().split(" "))
  tree[A].append(B)
  tree[B].append(A)

def DFS(node) :
  sum = 1
  check[node] = True
  
  for i in tree[node] :
    if not check[i] :
      sum += DFS(i)
  
  dp[node] = sum
  return sum

DFS(R)

for i in range(Q) :
  U = int(input())
  print(dp[U])
