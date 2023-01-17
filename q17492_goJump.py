import sys
from collections import deque
input = sys.stdin.readline

direction = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

N = int(input())
board = []
go = deque()


for i in range(N):
  board.append(list(map(int, input().split(" "))))
  for j in range(N) :
    if board[i][j] == 2 :
      go.append([i, j])

def DFS() :
  sum = 0
  for i in range(N) :
    sum += board[i].count(2)
  
  if sum == 1 :
    return True

  for i in range(N) :
    for j in range(N) :
      if board[i][j] == 2 :
        y, x = i, j
        for dir in direction :
          y_next = y + 2 * dir[0]
          x_next = x + 2 * dir[1]
          if y_next >= 0 and y_next < N and x_next >= 0 and x_next < N :
            if board[y_next][x_next] == 0 :
              y_check = y + dir[0]
              x_check = x + dir[1]
              if board[y_check][x_check] == 2 :
                board[y_check][x_check] = 0
                board[y][x] = 0
                board[y_next][x_next] = 2
                
                result = DFS()
                
                if result is True :
                  return True

                board[y_check][x_check] = 2
                board[y][x] = 2
                board[y_next][x_next] = 0
     
  return False

if DFS() is True :
  print("Possible")
else :
  print("Impossible")