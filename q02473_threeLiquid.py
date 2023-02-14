import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split(" ")))
liquid = sorted(liquid)

liquid.append(1e9)
liquid.append(-1e9)

def printResult(a, b, c) :
  result = [a, b, c]
  result = sorted(result)
  print("%d %d %d"%(result[0], result[1], result[2]))

if N == 3 :
  print("%d %d %d"%(liquid[0], liquid[1], liquid[2]))
  exit(0)

result = [0, 1, 2]

for i in range(N) :
  for j in range(N) :
    if i == j :
      continue
    
    target = (liquid[i] + liquid[j]) * -1
    if target < 0 :
      cur = [i, j, -2]
    else :
      cur = [i, j, -1]

    left = 0
    right = N-1

    while left <= right :
      mid = (left + right) // 2
      
      if mid != i and mid != j and target == liquid[mid] :
        printResult(liquid[i], liquid[j], liquid[mid])
        exit(0)

      if mid != i and mid != j and abs(target - liquid[cur[2]]) > abs(target - liquid[mid]) :
        cur[2] = mid
      
      if liquid[mid] < target :
        left = mid + 1
      else :
        right = mid - 1
    
    if abs(liquid[result[0]] + liquid[result[1]] + liquid[result[2]]) > abs(liquid[cur[0]] + liquid[cur[1]] + liquid[cur[2]]) :
      result = cur
    
printResult(liquid[result[0]], liquid[result[1]], liquid[result[2]])