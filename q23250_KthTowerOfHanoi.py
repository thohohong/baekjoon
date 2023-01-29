import sys
input = sys.stdin.readline

count = 0

def hanoi(start, ready, target, N):
  global count
  if N == 0 :
    return
  nextCost = pow(2, N-1) - 1
  if count + nextCost >= K :
    hanoi(start, target, ready, N-1)
  else :
    count += nextCost

  count += 1
  if count == K :
    print("%d %d"%(start, target))
    exit(0)

  if count + nextCost >= K :
    hanoi(ready, start, target, N-1)
  else :
    count += nextCost

N, K = map(int, input().split(" "))
hanoi(1, 2, 3, N)