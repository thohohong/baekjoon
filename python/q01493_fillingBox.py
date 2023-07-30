import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
cube = deque()

l, w, h = map(int, input().split(" "))
N = int(input())

for i in range(N) :
  A, B = map(int, input().split(" "))
  cube.appendleft([pow(2, A), B])

def devide(l, w, h, square) :
  # sort l, w, h
  h, w, l = sorted([l, w, h])
  
  while (l < square or w < square or h < square) and square > 1 :
    square /= 2

  if l == w == h :
    isPossible = False
    for cur in cube :
      if cur[1] == 0 :
        continue
      if cur[0] == l :
        cur[1] -= 1
        return 1
      elif cur[0] < l :
        isPossible = True
    if not isPossible :
      return -1
    square /= 2
  
  square = int(square)
  sum = 0
  result1 = devide(square, w, h, square)
  result2 = devide(l-square, w, h, square)

  if result1 == -1 or result2 == -1 :
    return -1
  else :
    sum = result1 + result2
    return sum
  
  # find largest cube that can be in this box
  for cur in cube :
    if cur[1] == 0 :
      continue
    if l == cur[0] and w == cur[0] and h == cur[0] :
      cur[1] -= 1
      return 1
    if h >= cur[0] :
      sum = 0

      result = devide(cur[0], w, h)
      if result == -1 :
        return -1
      else :
        sum += result

      result = devide(l-cur[0], w, h)
      if result == -1 :
        return -1
      else :
        sum += result

      return sum

  return -1

result = devide(l, w, h, 2**20)
print(result)