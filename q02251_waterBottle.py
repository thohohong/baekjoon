from collections import deque
visit = [] 
result = set()

a, b, c, = map(int, input().split(" "))

queue = deque()
queue.append((0, 0, c))

while not len(queue) == 0 :
    cur = queue.popleft()

    if cur in visit :
        continue

    visit.append(cur)
    if cur[0] == 0 :
        result.add(cur[2])

    # a to b
    new_a = cur[0] + cur[1] - b if cur[0] + cur[1] >= b else 0
    new_b = b if cur[0] + cur[1] >= b else cur[0] + cur[1]
    new_c = cur[2]

    queue.append((new_a, new_b, new_c))
    
    # a to c
    new_a = cur[0] + cur[2] - c if cur[0] + cur[2] >= c else 0
    new_b = cur[1]
    new_c = c if cur[0] + cur[2] >= c else cur[0] + cur[2]
    
    queue.append((new_a, new_b, new_c))

    # b to a
    new_a = a if cur[0] + cur[1] >= a else cur[0] + cur[1]
    new_b = cur[0] + cur[1] - a if cur[0] + cur[1] >= a else 0
    new_c = cur[2]

    queue.append((new_a, new_b, new_c))

    # b to c
    new_a = cur[0]
    new_b = cur[1] + cur[2] - c if cur[1] + cur[2] >= c else 0
    new_c = c if cur[1] + cur[2] >= c else cur[1] + cur[2]
    
    queue.append((new_a, new_b, new_c))

    # c to a
    new_a = a if cur[0] + cur[2] >= a else cur[0] + cur[2]
    new_b = cur[1]
    new_c = cur[0] + cur[2] - a if cur[0] + cur[2] >= a else 0

    queue.append((new_a, new_b, new_c))

    # c to b
    new_a = cur[0]
    new_b = b if cur[1] + cur[2] >= b else cur[1] + cur[2]
    new_c = cur[1] + cur[2] - b if cur[1] + cur[2] >= b else 0

    queue.append((new_a, new_b, new_c))

sorted_result = sorted(list(result))

for i in sorted_result : 
    print(i, end=" ")