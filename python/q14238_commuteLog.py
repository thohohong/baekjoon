import sys

input = sys.stdin.readline

S = input()

count = [0 for i in range(3)]

count[0] = S.count("A")
count[1] = S.count("B")
count[2] = S.count("C")

A, B, C = 0, 1, 2

intToChar = {0: 'A', 1: 'B', 2: 'C', -1:''}


dp = [[[[[True for p2 in range(4)] for p in range(4)] for c in range(count[C] + 1)] for b in range(count[B] + 1)] for a in range(count[A] + 1)]

def DFS(cur, pre) :
  if dp[count[A]][count[B]][count[C]][pre][cur] == False :
    return False

  if count[A] == 0 and count[B] == 0 and count[C] == 0 :
    print(intToChar[cur], end="")
    return True

  # A
  if count[A] > 0 :
    count[A] -= 1
    success = DFS(A, cur)
    count[A] += 1

    if success :
      print(intToChar[cur], end="")
      return True

  # B
  if cur != B and count[B] > 0:
    count[B] -= 1
    success = DFS(B, cur)
    count[B] += 1

    if success :
      print(intToChar[cur], end="")
      return True

  # C
  if pre != C and cur != C and count[C] > 0:
    count[C] -= 1
    success = DFS(C, cur)
    count[C] += 1
    
    if success :
      print(intToChar[cur], end="")
      return True
  
  dp[count[A]][count[B]][count[C]][pre][cur] = False
  return False

result = DFS(-1, -1)
if not result :
  print(-1)