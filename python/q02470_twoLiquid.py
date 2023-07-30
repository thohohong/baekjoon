import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split(" ")))
liquid = sorted(liquid)

if N == 2 :
  print("%d %d"%(liquid[0], liquid[1]))
  exit(0)

result = [liquid[0], liquid[-1]]

for i in range(N) :
  if liquid[1] < 0 :
    cur = [liquid[i], -1e9]
  else :
    cur = [liquid[i], 1e9]
  
  if (liquid[i] < 0 and i < N-1) or i == 0:
    left = i + 1
    right = N - 1
  else :
    left = 0
    right = i - 1
  
  target = cur[0] * -1

  while left <= right :
    mid = (left + right) // 2
    
    if liquid[mid] == target :
      print("%d %d"%(cur[0], liquid[mid]))
      exit(0)
    
    if abs(cur[1] - target) > abs(liquid[mid] - target) :
      cur[1] = liquid[mid]

    if target > liquid[mid] :
      left = mid + 1
    else :
      right = mid - 1

  if abs(cur[1] + cur[0]) < abs(result[1] + result[0]) : 
    result = cur

if result[0] > result[1] :
  result[0], result[1] = result[1], result[0]
print("%d %d"%(result[0], result[1]))