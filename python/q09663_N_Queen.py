def recursion(location, i, N) :
  global count
  # check validation
  for idx in range(i) :
    if abs(i - idx) == abs(location[i] - location[idx]) :
      return
    if location[i] == location[idx] :
      return

  if i == N-1 : # Termination
    count += 1
  else :
    # call recursively
    for idx in range(N) :
      location[i+1] = idx
      recursion(location, i+1, N)
  
N = int(input())
count = 0

for i in range(N) :
  location = [-1 for a in range(N)]
  location[0] = i
  recursion(location, 0, N)

print(count)
