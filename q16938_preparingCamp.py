import sys
import heapq
from collections import deque

input = sys.stdin.readline

def findSet(i, j, curSum) :
  if i > j :
    if curSum >= L and curSum <= R :
      return 1
    else :
      return 0

  if curSum > R :
    return 0
  
  result = 0
  result += findSet(i + 1, j, curSum + questions[i])
  result += findSet(i + 1, j, curSum)

  return result

N, L, R, X = map(int, input().split(" "))

questions = []
questions = list(map(int, input().split(" ")))
questions.sort()

j = 0
result = 0

for i in range(N) :
  j = i + 1
  while j < N and questions[j] - questions[i] < X :
    j += 1
  
  while j < N :
    curSum = questions[i] + questions[j]
    result += findSet(i+1, j-1, curSum)
    j += 1

print(result)