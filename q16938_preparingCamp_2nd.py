import sys
input = sys.stdin.readline


def solve(check) :
  count = 0
  max_difficulty = 0
  min_difficulty = sys.maxsize

  for i in range(N) :
    compare = 1 << i
    if compare & check :
      count += questions[i]
      max_difficulty = max(max_difficulty, questions[i])
      min_difficulty = min(min_difficulty, questions[i])

      if count > R :
        return False
  
  if count < L :
    return False
  
  if max_difficulty - min_difficulty < X :
    return False

  return True


N, L, R, X = map(int, input().split(" "))

questions = []
questions = list(map(int, input().split(" ")))

check = (1 << N) - 1

count = 0
while check > 0 :
  if solve(check) :
    count += 1
  check -= 1

print(count)