import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))

front = []
side = []

for i in range(N) :
  front.append(int(input()))

for i in range(M) :
  side.append(int(input()))

front.sort(reverse=True)
side.sort(reverse=True)
front.append(0)
side.append(0)

if front[0] != side[0] :
  print(-1)
  exit(0)

# minimum
i = 0
j = 0
minimum = 0

while i < N or j < M :
  if front[i] == side[j] :
    minimum += front[i]
    i += 1
    j += 1
  elif front[i] > side[j] :
    minimum += front[i]
    i += 1
  else :
    minimum += side[j]
    j += 1
  if i > N :
    i = N
  if j > M :
    j = M

# maximum
i = 0
j = 0
maximum = 0
while i < N or j < M :
  if front[i] == side[j] :
    maximum += front[i] * ((i + 1) * (j + 1) - i * j)
    i += 1
    j += 1
  elif front[i] > side[j] :
    maximum += front[i] * j
    i += 1
  else : 
    maximum += side[j] * i
    j += 1
  if i > N :
    i = N
  if j > M :
    j = M

print("%d %d"%(minimum, maximum))