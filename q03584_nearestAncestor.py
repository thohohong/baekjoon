import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T) :
  N = int(input())
  
  parents = [-1 for i in range(N+1)]

  for i in range(N-1) :
    A, B = map(int, input().split(" "))
    parents[B] = A

  n1, n2 = map(int, input().split(" "))
  
  n1_ancestor = []
  cur = n1

  while cur != -1 :
    n1_ancestor.append(cur)
    cur = parents[cur]
    
  cur = n2
  result = -1
  while cur != -1 :
    if cur in n1_ancestor :
      result = cur
      break
    cur = parents[cur]
  
  print(result)