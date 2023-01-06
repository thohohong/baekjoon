import sys
input = sys.stdin.readline

def reflect(dir) :
  if dir == 'R' :
    return 'L'
  elif dir == 'L' :
    return 'R'
  elif dir == 'D' :
    return 'U'
  elif dir == 'U' :
    return 'D'

def move2line_straight(C, firstDir) :
  answer = []
  curDir = firstDir
  for i in range(C-1) :
    answer.append(curDir)
  answer.append('D')
  curDir = reflect(curDir)
  for i in range(C-1) :
    answer.append(curDir)
  
  return ''.join(answer)
  
def move2line_zigzag(C, avoidY, avoidX) :
  answer = []
  curDir = 'D'
  x, y = 0, 0
  while True :
    nextY = y + dir[curDir][0]
    nextX = x + dir[curDir][1]

    if (nextX, nextY) == (avoidX, avoidY) :
      answer.append('R')
      x += 1
    elif (nextX, nextY) == (C - 1, 1) :
      answer.append(curDir)
      break
    else :
      x = nextX + 1
      y = nextY
      answer.append(curDir)
      answer.append('R')

      if (x, y) == (C - 1, 1) :
        break

      curDir = reflect(curDir)


  return ''.join(answer)


def evenCase(R, C, avoidY, avoidX) :
  isAvoided = False
  answer = []

  for i in range(R // 2) :
    if avoidY == i * 2 or avoidY == i * 2 + 1 :
      answer.append(move2line_zigzag(C, avoidY - i * 2, avoidX))
      isAvoided = True
    else :
      if isAvoided :
        answer.append(move2line_straight(C, 'L'))
      else :
        answer.append(move2line_straight(C, 'R'))
    
    if i != (R // 2) - 1 :
      answer.append('D')

  return ''.join(answer)

def oddCase(dir, firstDir, nextLevel, R, C) :
  answer = []
  curDir = firstDir
  x, y = 0, 0

  while True :
    nextY = y + dir[curDir][0]
    nextX = x + dir[curDir][1]
    
    if (nextY, nextX) == (R-1, C-1) :
      answer.append(curDir)
      break
    
    if nextY < 0 or nextY >= R or nextX < 0 or nextX >= C :
      answer.append(nextLevel)
      y = y + dir[nextLevel][0]
      x = x + dir[nextLevel][1]
      curDir = reflect(curDir)
    else :
      answer.append(curDir)
      y = nextY
      x = nextX
  return ''.join(answer)


dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
dir_reverse = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
R, C = map(int, input().split(" "))

field = []
minValue = 1e9
minCoordinate = None

for i in range(R) :
  field.append(list(map(int, input().split(" "))))
  for j in range(C) :
    if (i + j) % 2 == 1 and minValue > field[i][j] :
      minValue = field[i][j]
      minCoordinate = (i, j)

answer = []

if R % 2 == 1 :
  answer = oddCase(dir, 'R', 'D', R, C)
elif C % 2 == 1 :
  answer = oddCase(dir_reverse, 'D', 'R', R, C)
else :
  answer = evenCase(R, C, minCoordinate[0], minCoordinate[1])

print(answer)