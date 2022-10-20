from collections import deque

testCase = int(input(""))

move = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2))

for t in range(testCase):
  width = int(input(""))

  visit = [[False for col in range(width)] for row in range(width)]
  
  userInput = input("").split(" ")
  cur_x, cur_y = int(userInput[0]), int(userInput[1])

  userInput = input("").split(" ")
  goal_x, goal_y = int(userInput[0]), int(userInput[1])

  visit[cur_y][cur_x] = True

  q = deque()
  q.append((cur_y, cur_x, 0))

  while not len(q) == 0 :
    cur = q.popleft()
    
    if (cur[0], cur[1]) == (goal_y, goal_x) :
      print(cur[2])
      break

    for m in move :
      new_x = cur[1] + m[1]
      new_y = cur[0] + m[0]
      if new_x >= 0 and new_x < width and new_y >= 0 and new_y < width and not visit[new_y][new_x] :
        q.append((new_y, new_x, cur[2] + 1))
        visit[new_y][new_x] = True