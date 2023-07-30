import sys

def checkLine(line, N) :
    isNeedRamp = False
    length = 1

    for j in range(1, N) :
        heightDiff = line[j-1] - line[j] # heightDiff == 0 : same height, heightDiff > 0 : get lower, heightDiff < 0 : get higher
        if abs(heightDiff) >= 2 :
            isNeedRamp = False
            length = 1
            return False
        if heightDiff < 0 :
            if isNeedRamp or length < L:
                return False
            length = 1
        elif heightDiff == 0 :
            if isNeedRamp and length == L :
                isNeedRamp = False
                length = 0
            length += 1
        else :
            if isNeedRamp and length < L :
                return False
            isNeedRamp = True
            length = 1
    
    if isNeedRamp and length < L :
        return False
    else :
        return True

input = sys.stdin.readline

N, L = map(int, input().split(" "))

field = [[] for j in range(N)]

for i in range(N) :
    field[i] = list(map(int, input().split(" ")))


count = 0
test = []

# check row
for i in range(0, N) :
    if checkLine(field[i], N) :
        count += 1

for i in range(0, N) :
    newLine = []
    for j in range(N) :
        newLine.append(field[j][i])
    if checkLine(newLine, N) :
        count += 1
    
print(count)