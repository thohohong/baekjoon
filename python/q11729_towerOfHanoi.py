import sys

input = sys.stdin.readline

N = int(input())

def hanoi(start, ready, target, N) :
  if N == 0 :
    return
  hanoi(start, target, ready, N-1)
  print("%d %d"%(start, target))
  hanoi(ready, start, target, N-1)

print(pow(2, N) - 1)
hanoi(1, 2, 3, N)