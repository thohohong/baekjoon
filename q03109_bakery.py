import sys
input = sys.stdin.readline

R, C = map(int, input().split(" "))
field = []
for i in range(R) :
    field.append(list(input().strip()))

DIR = (-1, 0, 1)

def findPath(x, y) :
    if x == C - 1 :
        return True
    
    field[y][x] = 'x'

    for dir in DIR :
        nextY = y + dir
        if nextY < 0 or nextY >= R or field[nextY][x+1] == 'x' : # out of range
            continue

        isSuccess = findPath(x+1, nextY)
        if isSuccess :
            return True
    return False

pipelineNum = 0
for i in range(R) :
    if findPath(0, i) :
        pipelineNum += 1

print(pipelineNum)    