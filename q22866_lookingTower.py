def findCloserBuilding(a, b1, b2) :
    if abs(b1 - a) < abs(b2 - a) :
        return b1
    elif abs(b1 - a) == abs(b2 - a) :
        return b1 if b1 < b2 else b2
    else :
        return b2

N = int(input())
building = list(map(int, input().split(" ")))

leftEyesight = [0 for i in range(N)] # number of 
rightEyesight = [0 for i in range(N)]
closestBuilding = [200000 for i in range(N)]

stack = []

# detect left side
for i in range(N) :
    while len(stack) != 0 and stack[-1][0] <= building[i] :
        stack.pop()
    leftEyesight[i] = len(stack)
    if len(stack) != 0 :
        closestBuilding[i] = findCloserBuilding(i, closestBuilding[i], stack[-1][1])
    stack.append((building[i], i))

stack = []

# detect right side
for i in range(N-1, -1, -1) :
    while len(stack) != 0 and stack[-1][0] <= building[i] :
        stack.pop()
    rightEyesight[i] = len(stack)
    if len(stack) != 0 :
        closestBuilding[i] = findCloserBuilding(i, closestBuilding[i], stack[-1][1])
    stack.append((building[i], i))

# print
for i in range(N):
    print(leftEyesight[i] + rightEyesight[i], end="")
    if (leftEyesight[i] + rightEyesight[i] != 0) :
        print("", end=" ")
        print(closestBuilding[i]+1)
    else :
        print("")