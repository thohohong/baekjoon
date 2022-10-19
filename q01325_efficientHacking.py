from collections import deque

def find(a):
  answer = 0
  visit = [False for i in range(N+1)]
  queue = deque()

  queue.append(a)
  visit[a] = True
  while(not len(queue) == 0):
    # print(visit)
    item = queue.popleft()
    answer += 1
    
    for i in computers[item]:
      if not visit[i] :
        queue.append(i)
        visit[i] = True
  
  return answer
    

input_ = input("").split()

N = int(input_[0])
M = int(input_[1])

#check = [False for i in range(N+1)]

computers = [[] for i in range(N+1)]

for i in range(M):
  input_ = input("").split()
  A = int(input_[0])
  B = int(input_[1])
  computers[B].append(A)

hacknum = [0 for i in range(N+1)]

for i in range(1, N+1) :
  hacknum[i] = find(i)

maxNum = max(hacknum)

for i in range(1, N+1):
  if hacknum[i] == maxNum :
    print(i, end=" ")
