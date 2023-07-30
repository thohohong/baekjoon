import sys
input = sys.stdin.readline

def recursive(y, x, n) :
  if n == 1 :
    print(vid[y][x], end="")
    return
  
  check = vid[y][x]
  isDiff = False
  for i in range(y, y+n) :
    for j in range(x, x+n) :
      if vid[i][j] != check :
        isDiff = True
        break
    if isDiff :
      break
  
  if isDiff :
    nextN = n//2
    print("(", end="")
    recursive(y, x, nextN)
    recursive(y, x + nextN, nextN)
    recursive(y + nextN, x, nextN)
    recursive(y + nextN, x + nextN, nextN)
    print(")", end="")
  else :
    print(check, end="")

N = int(input())

vid = []
for i in range(N) :
  line = list(map(int, list(input().strip())))
  vid.append(line)

recursive(0, 0, N)
